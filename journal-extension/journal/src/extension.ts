import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';
import * as yaml from 'js-yaml';

export function activate(context: vscode.ExtensionContext) {
    console.log('Your extension "journalExtension" is now active!');

    const disposable = vscode.commands.registerCommand('journalExtension.createJournalEntry', () => {
        createJournalEntry();
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}

function createJournalEntry() {
    const rootPath = vscode.workspace.rootPath;
    if (!rootPath) {
        vscode.window.showErrorMessage('No open folder/workspace detected');
        return;
    }

    const date = new Date();
    const year = date.getFullYear().toString();
    const monthShort = date.toLocaleString('default', { month: 'short' });
    const monthLong = date.toLocaleString('default', { month: 'long' });
    const day = date.getDate().toString().padStart(2, '0');
    const isoDate = date.toISOString().split('T')[0]; // YYYY-MM-DD format

    const journalPath = path.join(rootPath, 'journal', year, monthShort);
    const journalFile = path.join(journalPath, `${day}${monthShort}${year}.md`);

    // Create directory structure
    if (!fs.existsSync(journalPath)) {
        fs.mkdirSync(journalPath, { recursive: true });
    }

    if (!fs.existsSync(journalFile)) {
        const fileContent = `---
date: "${isoDate}"
title: "Daily Journal - ${day} ${monthShort} ${year}"
---

`;
        fs.writeFileSync(journalFile, fileContent);
        updateMystYaml(year, monthShort);
        openFile(journalFile);
    } else {
        vscode.window.showInformationMessage('Journal entry for today already exists.');
        openFile(journalFile);
    }
}

function updateMystYaml(year: string, month: string) {
    const rootPath = vscode.workspace.rootPath;
    if (!rootPath) return;

    const mystYamlPath = path.join(rootPath, 'myst.yml');
    if (!fs.existsSync(mystYamlPath)) return;

    try {
        const mystContent = fs.readFileSync(mystYamlPath, 'utf8');
        const mystConfig = yaml.load(mystContent) as any;

        // Find the journal section in the TOC
        const journalToc = mystConfig.project.toc.find((item: any) => item.file === 'journal.md');
        if (!journalToc) return;

        // Find or create the year section
        let yearSection = journalToc.children.find((child: any) => child.title === year);
        if (!yearSection) {
            yearSection = {
                title: year,
                children: []
            };
            journalToc.children.push(yearSection);
        }

        // Find or create the month section
        const monthLong = new Date(`${year}-${month}-01`).toLocaleString('default', { month: 'long' });
        let monthSection = yearSection.children.find((child: any) => child.title === monthLong);
        if (!monthSection) {
            monthSection = {
                title: monthLong,
                children: []
            };
            yearSection.children.push(monthSection);
        }

        // Add the pattern if it doesn't exist
        const monthPattern = `journal/${year}/${month}/**{.ipynb,.md}`;
        const patternExists = monthSection.children.some((child: any) => 
            child.pattern === monthPattern
        );

        if (!patternExists) {
            monthSection.children.push({
                pattern: monthPattern
            });
        }

        // Write back the updated config
        fs.writeFileSync(mystYamlPath, yaml.dump(mystConfig));
    } catch (error: any) {
        vscode.window.showErrorMessage(`Failed to update myst.yml: ${error.message}`);
    }
}

function openFile(filePath: string): void {
    vscode.workspace.openTextDocument(filePath).then(doc => {
        return vscode.window.showTextDocument(doc);
    }).then(undefined, err => {
        vscode.window.showErrorMessage('Failed to open file: ' + err.message);
    });
}
