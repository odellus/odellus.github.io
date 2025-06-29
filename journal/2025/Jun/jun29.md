---
date: "2025-06-29"
title: "Cleaning house"
subtitle: "Automation is a lot of work"
---

# Cleaning up

I really want to get one of those roombas. I had one in Vegas and it was nice. I've got almost everything off the floor in the dining room and kitchen, but there's still a lot of work to do in the rest of the house. I figured I might as well clean top to bottom and I've been going through all of my Akro Mil bins and organizing them, throwing away stuff I don't need. Putting similar things in plastic bags so I can consolidate stuff. I've got a label maker but they're plastic bags I can just write on the outside of them what they are.


I threw away a lot of stuff that had been accumulating in the central hall yesterday and bought a swiffer duster so I've been running around for the past couple of hours gathering all of the random bits of hardware I don't want to throw away but don't have any use for that seem to have gathered on all of the surfaces in the house into a bag so I can just have the "furniture hardware/allen wrench" bag and dust around here.

# Refinancing

I really need to refinance. I bought when mortgages were 7% and I've been waiting for Powell to cut every since. I could have bought a nice car with the money I've spent on my 7% mortgage vs a reasonable rate since I've moved it.


Any damn day now. Shit even 6.625% would give me a few hundred back versus what I'm paying now. I saw one that wanted to give me cash out and I was paying way less a month versus what I'm at and I don't know I need to start looking into it. Looking like everybody wants to do refinance at 6.75%. 

:::{danger}FUCK
> THIS SUCKS!!!
:::


## Quit my bitching

Okay I'll refinance when it makes more sense for me to refinance and not through some nonsense offer that's going to screw me over because I didn't read the fine print. Anyway.

# Computational Developmental Systems Biology

Okay I've got this to review the state of the art in cell simulation and developmental biology so I don't tread water in computational systems biology when I know so much and have so much to offer. This needs to be the game I play. I need to be a world expert at this stuff, and after just a little while, a few tutorials here, an addition of something to the code there, and I will be! The point is to get started.

This would be a great


:::{warning} AI Generated Response
The following is a response to a query on you.com outlining my plan for an epigenetic waddington landscape database and simulation engine.
:::


---

# 🧬 Framework for Hypothesis Testing in Developmental Biology: Project Blueprint

> **Key Takeaway:**  
> You can build a powerful, future-proof platform for developmental biology by integrating flexible database architectures (MongoDB + Neo4j), leveraging major cell atlas resources, using Taichi for high-performance simulations, and adopting AI-driven literature review and data integration strategies. This approach will enable granular, mechanistic insights into organismal development.

---

### 1. **Database Architecture Recommendations**

**Hybrid Approach: MongoDB + Neo4j**

| Component         | Purpose                                                                 | Rationale                                                                                 |
|-------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **MongoDB**       | Store heterogeneous, evolving omics data (single-cell RNA, SNPs, imaging, metadata) | Flexible schema, high scalability, ideal for diverse and large-scale biological datasets  |
| **Neo4j**         | Model and query complex genetic regulatory networks and cell relationships | Efficient for deep, relationship-centric queries (e.g., pathway analysis, lineage tracing)  |
| **Integration**   | Use both in tandem: MongoDB for raw/processed data, Neo4j for network/relationship queries | Hybrid solutions are common in bioinformatics for comprehensive analysis             |

> **Key Finding:**  
> This hybrid architecture supports both flexible data storage and efficient network analysis, crucial for modeling the Waddington landscape and integrating multi-omic, spatial, and temporal data.

---

### 2. **Data Integration Strategy**

**Leverage Major Cell Atlas Initiatives and Multi-Omics Platforms**

- **Primary Data Sources:**
  - Human Cell Atlas (HCA) & Human Developmental Cell Atlas (HDCA) for human and developmental data 
  - Allen Brain Cell Atlas for brain-specific, multimodal data 
  - Arc Virtual Cell Atlas for multi-species, computation-ready single-cell data 
  - Model organism databases: FlyBase, ZFIN, MGI, WormBase, TAIR for Drosophila, zebrafish, mouse, C. elegans, and Arabidopsis 
- **Integration Tools:**
  - Use platforms like CZ CELLxGENE and Cytoscape/scNetViz for dataset harmonization and visualization 
  - Employ machine learning frameworks (e.g., scVI, scANVI) for batch correction and cross-study integration

> **Key Finding:**  
> Standardizing and harmonizing data from these resources will provide a rich, multi-dimensional foundation for simulation and hypothesis testing.

---

### 3. **Simulation Framework Design**

**Taichi for High-Performance, GPU-Accelerated Simulations**

- **Why Taichi?**
  - Native GPU support, automatic parallelization, and integration with Python ecosystem 
  - Proven use in molecular dynamics, agent-based, and particle-based biological simulations
  - Supports real-time, 3D cell imaging and spatially explicit modeling (e.g., diffusion, cell migration)
- **Simulation Modules:**
  - **Genetic Regulatory Network (GRN) Simulation:** Integrate with tools like GRiNS, GINsim, or BioTapestry for network logic and dynamics 
  - **Diffusion and Biophysical Modeling:** Implement custom modules for diffusion coefficients and spatial processes using Taichi’s particle/fluid simulation capabilities
  - **Cellular Imaging Integration:** Ingest and visualize real-time 3D imaging data for model validation and hypothesis generation

> **Key Finding:**  
> Taichi’s flexibility and performance make it ideal for simulating complex, multi-scale developmental processes, especially when combined with existing GRN modeling tools.

---

### 4. **Literature Review Methodology**

**AI-Assisted, Systematic Review Pipeline**

- **Automated Literature Mining:**
  - Use AI/NLP tools (e.g., PubMed APIs, semantic search engines) to extract relevant studies, datasets, and experimental results
  - Tag and index findings by organism, developmental stage, omics type, and experimental context
- **Expert Curation:**
  - Integrate human-in-the-loop review for quality control and hypothesis refinement
- **Continuous Updating:**
  - Set up automated alerts and periodic reviews to keep the database current with the latest research

> **Key Finding:**  
> Combining AI-driven mining with expert curation ensures comprehensive, up-to-date coverage of the rapidly evolving developmental biology literature.

---

### 5. **Technology Stack Selection**

| Layer                | Recommended Technology/Tool                | Justification                                                                 |
|----------------------|--------------------------------------------|-------------------------------------------------------------------------------|
| **Database**         | MongoDB, Neo4j                             | Hybrid for flexibility and network analysis                                   |
| **Data Integration** | Python (pandas, scVI, scANVI), Cytoscape   | Mature libraries for omics data harmonization and visualization               |
| **Simulation**       | Taichi, GRiNS, GINsim, BioTapestry         | High-performance, extensible, and compatible with Python ecosystem            |
| **Visualization**    | CZ CELLxGENE, custom 3D viewers (e.g., VTK, Plotly) | For interactive exploration of cell states and landscapes                     |
| **AI/ML**            | PyTorch, TensorFlow, HuggingFace Transformers | For literature mining, data integration, and model training                   |
| **Web/API**          | FastAPI, Flask, React                      | For user interface, data access, and integration with AI assistants           |

---

### 6. **Implementation Roadmap**

#### **Phase 1: Foundation**
- Set up MongoDB and Neo4j instances
- Ingest initial datasets from major cell atlases and model organism databases
- Develop data harmonization and integration pipelines

#### **Phase 2: Simulation Core**
- Build Taichi-based simulation modules for GRN dynamics and diffusion modeling
- Integrate with existing GRN tools (GRiNS, GINsim)
- Connect simulation outputs to database for storage and analysis

#### **Phase 3: Literature Integration**
- Deploy AI/NLP pipeline for automated literature mining and tagging
- Curate and link relevant studies to database entries

#### **Phase 4: Visualization & User Interface**
- Implement interactive dashboards for data exploration (CZ CELLxGENE, custom viewers)
- Enable real-time 3D visualization of simulation and imaging data

#### **Phase 5: AI Assistant Integration**
- Develop or integrate AI agents for expert feedback, hypothesis suggestion, and workflow automation

#### **Phase 6: Expansion & Community Engagement**
- Add support for new data types (e.g., spatial transcriptomics, proteomics)
- Open platform for community data contributions and benchmarking

---

## **Conclusion**

Your vision is not only feasible but aligns with the latest advances in computational synthetic biology, database technology, and AI-driven research. By combining a hybrid database architecture, leveraging open cell atlas resources, using Taichi for simulation, and integrating AI for literature review and expert feedback, you can create a robust, extensible framework for hypothesis testing in developmental biology. This platform will empower granular, mechanistic insights into organismal development and serve as a valuable resource for the scientific community.

---
:::{important}**Summary**  

- **Database:** MongoDB + Neo4j hybrid for flexible, scalable storage and network analysis  
- **Data:** Integrate from major cell atlases and model organism databases  
- **Simulation:** Taichi for high-performance, multi-scale modeling  
- **Literature:** AI-assisted, systematic review pipeline  
- **Stack:** Python ecosystem, open-source tools, web-based interfaces  
- **Roadmap:** Foundation → Simulation → Literature → Visualization → AI Integration → Expansion
:::
---

:::{tip}Human generated slop
The following slop has been generated by a  human being.
:::

# Wow! That's amazing.
Okay so I definitely need to dive deeper into the [Arc Virtual Cell Atlas][scBaseCount]. `scBaseCount` sounds like something I was planning on doing myself as part of the project specs so I might as well read about how they're doing it.


 [GRiNS][GRiNS] and the other simulation engines definitely look like something I should be reading about.

I created a project called [`epiwad`][you-epiwad] that the above walks through a very cursory first draft idea regarding the project. I have a lot of work to do just on reading the background material before I ever start putting together code. Many tutorials to follow. Honestly I'm putting all of this crap into books. They might just be shitty AI slop that I have some bot put together from the work I'm doing and the tutorials I'm going to reproduce in the interest of building on top of all the amazing work that's already been done and writing it up in an accessible way, but it will be something.


:::{figure} ../images/epiwad.png
First rough draft logo but I like it
:::

# TO DO

- Go over the links and references above more thoroughly
- Update plan with knowledge gained from deep dives into each of the subjects
- More queries into each specific aspect as the subject matter knowledge increases
- Continue to update plan
- Download and run all available tutorials
- Condense main points of paper into journal posts

[scBaseCount]: https://github.com/ArcInstitute/arc-virtual-cell-atlas/blob/main/scBaseCount/README.md
[GRiNS]: https://github.com/MoltenEcdysone09/GRiNS/blob/main/README.md
[you-epiwad]: https://you.com/projects/686184e2a9811bf5aada25c7