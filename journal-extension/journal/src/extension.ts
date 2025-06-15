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
    const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
    if (!workspaceRoot) {
        vscode.window.showErrorMessage('No open folder/workspace detected');
        return;
    }

    const today = new Date();
    const monthShort = today.toLocaleString('default', { month: 'short' }).toLowerCase();
    const monthCapitalized = monthShort.charAt(0).toUpperCase() + monthShort.slice(1);
    const day = today.getDate();
    const year = today.getFullYear();
    
    // Create the directory structure if it doesn't exist
    const yearDir = path.join(workspaceRoot, 'journal', year.toString());
    const monthDir = path.join(yearDir, monthCapitalized);
    
    if (!fs.existsSync(yearDir)) {
        fs.mkdirSync(yearDir, { recursive: true });
    }
    if (!fs.existsSync(monthDir)) {
        fs.mkdirSync(monthDir, { recursive: true });
    }
    
    // Create the file with the new naming convention: month+day.md
    const fileName = `${monthShort}${day}.md`;
    const filePath = path.join(monthDir, fileName);
    
    // Create the file content
    const content = `---
date: "${year}-${(today.getMonth() + 1).toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}"
title: "Daily Journal - ${day} ${monthCapitalized} ${year}"
---
`;
    
    fs.writeFileSync(filePath, content);
    
    // Update myst.yml with the new file
    updateMystYaml(year.toString(), monthCapitalized);
    
    // Open the file
    const openPath = vscode.Uri.file(filePath);
    vscode.workspace.openTextDocument(openPath).then(doc => {
        vscode.window.showTextDocument(doc);
    });
}

function updateMystYaml(year: string, month: string) {
    const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
    if (!workspaceRoot) return;

    const mystYamlPath = path.join(workspaceRoot, 'myst.yml');
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

        // Get all month directories for this year
        const yearDir = path.join(workspaceRoot, 'journal', year);
        if (!fs.existsSync(yearDir)) return;

        const months = fs.readdirSync(yearDir)
            .filter(dir => fs.statSync(path.join(yearDir, dir)).isDirectory())
            .sort((a, b) => {
                const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                return months.indexOf(a) - months.indexOf(b);
            });

        // Update the TOC to match the directory structure
        yearSection.children = months.map(monthDir => ({
            title: monthDir,
            children: [{
                pattern: `journal/${year}/${monthDir}/**{.ipynb,.md}`
            }]
        }));

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
