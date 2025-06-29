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

# Query:
> I want to create a framework for testing hypotheses in developmental biology using the known genetic regulatory networks and whatever kinds of diffusion coefficients and whatnot we can glean from single cell rna and snp studies the whole nine yards, histography with real time 3d cell imaging. I want to create a database for this kind of information surrounding the waddington landscape of the cells as they divide. I imagine there are several sources of information on cell atlases for developmental model organisms. I want to collect them into a place where they can be put through the paces of simulation and integration of real work -omic data from various sources, including mass scale lit review, to arrive as some ideas as to how organisms develop on a more granular level than we might currently understand.
> 
> 
> I think taichi is a good language for developing the simulation aspects. I don't know about the database side of things. I imagine the literature review aspect will take precedence.
>
>
> Does this make any sense? I eventually want to integrate AI assistants for expert feedback, but I need some kind of database of single cell omic studies that can connect with actual genetic regulatory network simulations of development, even if they're not full cell based. We need to investigate carefully cell simulation advances of computational synthetic biology

## 🧬 Framework for Hypothesis Testing in Developmental Biology: Project Blueprint

:::{tip}**Key Takeaway:**  
You can build a powerful, future-proof platform for developmental biology by 
-integrating flexible database architectures (MongoDB + Neo4j)
- leveraging major cell atlas resources
- using Taichi for high-performance simulations
- adopting AI-driven literature review and data integration strategies  

This approach will enable granular, mechanistic insights into organismal development.
:::
---

### 1. **Database Architecture Recommendations**

**Hybrid Approach: MongoDB + Neo4j**

| Component         | Purpose                                                                 | Rationale                                                                                 |
|-------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **MongoDB**       | Store heterogeneous, evolving omics data (single-cell RNA, SNPs, imaging, metadata) | Flexible schema, high scalability, ideal for diverse and large-scale biological datasets [[1]](https://medium.com/@prem.shah_15628/deep-dive-mongodb-vs-neo4j-vs-rdbms-a-technical-analysis-for-complex-biological-networks-e704df639e24#:~:text=MongoDB%E2%80%99s%20document%2Doriented%20architecture%20has,capable%20of%20handling%20the) |
| **Neo4j**         | Model and query complex genetic regulatory networks and cell relationships | Efficient for deep, relationship-centric queries (e.g., pathway analysis, lineage tracing) [[2]](https://medium.com/@marcoscedenillabonet/full-data-science-project-part-3-storage-architecture-with-mongodb-and-neo4j-a8ce87a4535a#:~:text=The%20combination%20of%20MongoDB,dataset%20of%20scientific%20articles) |
| **Integration**   | Use both in tandem: MongoDB for raw/processed data, Neo4j for network/relationship queries | Hybrid solutions are common in bioinformatics for comprehensive analysis [[3]](https://arcinstitute.org/news/arc-virtual-cell-atlas-launch#:~:text=Arc%20Institute%20today%20launched,initial%20release%20of%20the)            |

:::{important}**Key Finding:**  
This hybrid architecture supports both flexible data storage and efficient network analysis, crucial for modeling the Waddington landscape and integrating multi-omic, spatial, and temporal data.
:::
---

### 2. **Data Integration Strategy**

**Leverage Major Cell Atlas Initiatives and Multi-Omics Platforms**

- **Primary Data Sources:**
  - Human Cell Atlas (HCA) & Human Developmental Cell Atlas (HDCA) for human and developmental data [[4]](https://www.humancellatlas.org/#:~:text=The%20Human%20Cell%20Atlas,to%20transform%20our%20understanding)[[5]](https://www.humancellatlas.org/biological-networks/development-biological-network/#:~:text=comprehensive%20profile%20of%20these,as%20well%20as%20ageing.)
  - Allen Brain Cell Atlas for brain-specific, multimodal data [[6]](https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas#:~:text=The%20Allen%20Brain%20Cell,data%20across%20the%20mammalian)
  - Arc Virtual Cell Atlas for multi-species, computation-ready single-cell data [[3]](https://arcinstitute.org/news/arc-virtual-cell-atlas-launch#:~:text=Arc%20Institute%20today%20launched,initial%20release%20of%20the)
  - Model organism databases: FlyBase, ZFIN, MGI, WormBase, TAIR for Drosophila, zebrafish, mouse, C. elegans, and Arabidopsis [[7]](http://flycellatlas.org/#:~:text=The%20Fly%20Cell%20Atlas,epigenomics%2C%20to%20build%20comprehensive)[[8]](https://bioinfo.cd-genomics.com/model-organism-databases.html#:~:text=provides%20a%20well%2Ddocumented%20phenotypic%2C,and%20segments%2C%20maps%20and)[[9]](https://bioinfo.cd-genomics.com/model-organism-databases.html#:~:text=%E2%88%92%20Zebrafish%20Information%20Network,curated%2C%20organized%20and%20cross%2Dreferenced)[[10]](https://bioinfo.cd-genomics.com/model-organism-databases.html#:~:text=%E2%88%92%20The%20Arabidopsis%20Information,TAIR%20includes%20the%20complete)
- **Integration Tools:**
  - Use platforms like CZ CELLxGENE and Cytoscape/scNetViz for dataset harmonization and visualization [[11]](https://cellxgene.cziscience.com/#:~:text=Chan%20Zuckerberg%20CELLxGENE%20Discover,and%20standardized%20single%2Dcell%20biology)[[12]](https://chanzuckerberg.com/human-cell-atlas/human-cell-atlas-integration-with-the-cytoscape-ecosystem-for-analysis-of-scrna-seq-data/#:~:text=The%20Morris%20lab%20developed,EBI%20Single%2DCell%20Expression%20Atlas)
  - Employ machine learning frameworks (e.g., scVI, scANVI) for batch correction and cross-study integration

:::{warning}**Key Finding:**  
Standardizing and harmonizing data from these resources will provide a rich, multi-dimensional foundation for simulation and hypothesis testing.
:::
---

### 3. **Simulation Framework Design**

**Taichi for High-Performance, GPU-Accelerated Simulations**

- **Why Taichi?**
  - Native GPU support, automatic parallelization, and integration with Python ecosystem [[13]](https://docs.taichi-lang.org/blog/what-taichi-is-capable-of#:~:text=and%20designed%20for%20high%2Dperformance,community.%20From%20an%20immature)
  - Proven use in molecular dynamics, agent-based, and particle-based biological simulations
  - Supports real-time, 3D cell imaging and spatially explicit modeling (e.g., diffusion, cell migration)
- **Simulation Modules:**
  - **Genetic Regulatory Network (GRN) Simulation:** Integrate with tools like GRiNS, GINsim, or BioTapestry for network logic and dynamics [[14]](http://ginsim.org/#:~:text=GINsim%20%28Gene%20Interaction%20Network,simulation%20of%20genetic%20regulatory)[[15]](https://arxiv.org/abs/2503.18356#:~:text=GRiNS%20integrates%20popular%20parameter%2Dagnostic,library%20capable%20of%20leveraging)
  - **Diffusion and Biophysical Modeling:** Implement custom modules for diffusion coefficients and spatial processes using Taichi’s particle/fluid simulation capabilities
  - **Cellular Imaging Integration:** Ingest and visualize real-time 3D imaging data for model validation and hypothesis generation

:::{tip}**Key Finding:**  
Taichi’s flexibility and performance make it ideal for simulating complex, multi-scale developmental 
processes, especially when combined with existing GRN modeling tools.
:::
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

:::{note}**Key Finding:**  
Combining AI-driven mining with expert curation ensures comprehensive, up-to-date coverage of the rapidly evolving developmental biology literature.
:::
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

:::{attention}**Summary Box:**  
- **Database:** MongoDB + Neo4j hybrid for flexible, scalable storage and network analysis  
- **Data:** Integrate from major cell atlases and model organism databases  
- **Simulation:** Taichi for high-performance, multi-scale modeling  
- **Literature:** AI-assisted, systematic review pipeline  
- **Stack:** Python ecosystem, open-source tools, web-based interfaces  
- **Roadmap:** Foundation → Simulation → Literature → Visualization → AI Integration → Expansion
:::
---




### Links

1. **GINsim | Qualitative analysis of regulatory networks: a ...**. [http://ginsim.org](http://ginsim.org/#:~:text=GINsim%20%28Gene%20Interaction%20Network,simulation%20of%20genetic%20regulatory)
2. **BioTapestry**. [https://biotapestry.systemsbiology.net](https://biotapestry.systemsbiology.net/#:~:text=BioTapestry%20is%20an%20interactive,and%20simulating%20genetic%20regulatory)
3. **SPREd: a simulation-supervised neural network tool for gene ...**. [https://academic.oup.com](https://academic.oup.com/bioinformaticsadvances/article/4/1/vbae011/7587436#:~:text=SPRED%3A%20a%20simulation%2Dsupervised%20learning,ML%20models%20of%20the)
4. **GRiNS: A Python Library for Simulating Gene Regulatory ...**. [https://arxiv.org](https://arxiv.org/abs/2503.18356#:~:text=GRiNS%20integrates%20popular%20parameter%2Dagnostic,library%20capable%20of%20leveraging)
5. **Ingeneue: a software tool to simulate and explore genetic ...**. [https://pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/19399429/#:~:text=Here%20I%20describe%20how,models%20of%20gene%20regulatory)
6. **Current approaches to gene regulatory network modelling**. [https://pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC1995542/#:~:text=We%20proposed%20the%20following,control%20logic%20models%2C%20and)
7. **An Intuitive Tool for Constructing and Evaluating Gene ...**. [https://www.biorxiv.org](https://doi.org/10.1101/2024.12.18.629005)
8. **From molecular simulation to black hole rendering - Taichi Docs**. [https://docs.taichi-lang.org](https://docs.taichi-lang.org/blog/what-taichi-is-capable-of#:~:text=and%20designed%20for%20high%2Dperformance,community.%20From%20an%20immature)
9. **From molecular simulation to black hole rendering - Taichi Docs**. [https://docs.taichi-lang.org](https://docs.taichi-lang.org/blog/what-taichi-is-capable-of#:~:text=%2D%20Supports%20multiple%20backends%2C,Metal%2C%20and%20OpenGL%20Compute)
10. **victoriacity/taichimd: Interactive, GPU-accelerated ...**. [https://github.com](https://github.com/victoriacity/taichimd#:~:text=%2D%20To%20provide%20a,simulation%20algorithms%20and%20machine%2Dlearned)
11. **victoriacity/taichimd: Interactive, GPU-accelerated ...**. [https://github.com](https://github.com/victoriacity/taichimd#:~:text=%2D%20Incorporate%20agent%2Dbased%20simulation%20algorithms%20%28crowd%20simulation%2C%20particle%20swarm%29%20and%20optimization%2Dbased%20integrators)
12. **Human Cell Atlas**. [https://www.humancellatlas.org](https://www.humancellatlas.org/#:~:text=The%20Human%20Cell%20Atlas,to%20transform%20our%20understanding)
13. **Human Cell Atlas Integration with the Cytoscape ...**. [https://chanzuckerberg.com](https://chanzuckerberg.com/human-cell-atlas/human-cell-atlas-integration-with-the-cytoscape-ecosystem-for-analysis-of-scrna-seq-data/#:~:text=The%20Morris%20lab%20developed,EBI%20Single%2DCell%20Expression%20Atlas)
14. **Allen Brain Cell Atlas**. [https://portal.brain-map.org](https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas#:~:text=The%20Allen%20Brain%20Cell,data%20across%20the%20mammalian)
15. **Allen Brain Atlas: Cell Types: Overview**. [https://celltypes.brain-map.org](https://celltypes.brain-map.org/#:~:text=The%20database%20contains%20electrophysiological%2C,as%20models%20simulating%20cell)
16. **Cell Types Database: RNA-Seq Data**. [https://portal.brain-map.org](https://portal.brain-map.org/atlases-and-data/rnaseq#:~:text=This%20data%20set%20includes,human%20and%20mouse%20brain)
17. **Whole Mouse Brain Atlas - Brain Cell Data Center (BCDC)**. [https://www.biccn.org](https://www.biccn.org/science/whole-mouse-brain#:~:text=The%20first%20complete%20cell,from%20the%20adult%20mouse)
18. **Arc Virtual Cell Atlas launches, combining data from over ...**. [https://arcinstitute.org](https://arcinstitute.org/news/arc-virtual-cell-atlas-launch#:~:text=Arc%20Institute%20today%20launched,initial%20release%20of%20the)
19. **Arc Virtual Cell Atlas launches, combining data from over ...**. [https://arcinstitute.org](https://arcinstitute.org/news/arc-virtual-cell-atlas-launch#:~:text=by%20Tahoe%20%28formerly%20Vevo,first%20single%2Dcell%20RNA%20sequencing)
20. **Development Biological Network**. [https://www.humancellatlas.org](https://www.humancellatlas.org/biological-networks/development-biological-network/#:~:text=comprehensive%20profile%20of%20these,as%20well%20as%20ageing.)
21. **Human Developmental Cell Atlas | Single cell atlas of the ...**. [https://developmental.cellatlas.io](https://developmental.cellatlas.io/#:~:text=profile%20of%20these%20cell,well%20as%20ageing.%20Furthermore%2C)
22. **Model Organism Databases**. [https://bioinfo.cd-genomics.com](https://bioinfo.cd-genomics.com/model-organism-databases.html#:~:text=provides%20a%20well%2Ddocumented%20phenotypic%2C,and%20segments%2C%20maps%20and)
23. **Model Organism Databases**. [https://bioinfo.cd-genomics.com](https://bioinfo.cd-genomics.com/model-organism-databases.html#:~:text=%E2%88%92%20Zebrafish%20Information%20Network,curated%2C%20organized%20and%20cross%2Dreferenced)
24. **FLY CELL ATLAS - FlyCellAtlas description.**. [http://flycellatlas.org](http://flycellatlas.org/#:~:text=The%20Fly%20Cell%20Atlas,epigenomics%2C%20to%20build%20comprehensive)
25. **Model Organism Databases**. [https://bioinfo.cd-genomics.com](https://bioinfo.cd-genomics.com/model-organism-databases.html#:~:text=%E2%88%92%20The%20Arabidopsis%20Information,TAIR%20includes%20the%20complete)
26. **Databases & Protocols**. [https://www.cshl.edu](https://www.cshl.edu/cshl-library/resources/databases-protocols/#:~:text=The%20Arabidopsis%20Information%20Resource,data%20for%20Arabidopsis%20thaliana%2C)
27. **Plant Cell Atlas**. [https://www.plantcellatlas.org](https://www.plantcellatlas.org/#:~:text=PCA%20Initiative%E2%80%8B%E2%80%8B%20The%20Plant,cell%20types%20and%20integrates)
28. **The Biodiversity Cell Atlas: charting cellular diversity on Earth**. [https://www.ebi.ac.uk](https://www.ebi.ac.uk/about/news/announcements/the-biodiversity-cell-atlas-charting-cellular-diversity-on-earth#:~:text=The%20Biodiversity%20Cell%20Atlas,chart%20cell%20types%20across)
29. **CZ CELLxGENE Discover - Cellular Visualization Tool**. [https://cellxgene.cziscience.com](https://cellxgene.cziscience.com/#:~:text=Chan%20Zuckerberg%20CELLxGENE%20Discover,and%20standardized%20single%2Dcell%20biology)
30. **Deep Dive: MongoDB vs Neo4j vs RDBMS — A Technical ...**. [https://medium.com](https://medium.com/@prem.shah_15628/deep-dive-mongodb-vs-neo4j-vs-rdbms-a-technical-analysis-for-complex-biological-networks-e704df639e24#:~:text=MongoDB%E2%80%99s%20document%2Doriented%20architecture%20has,capable%20of%20handling%20the)
31. **Full Data Science Project Part 3: Storage Architecture with ...**. [https://medium.com](https://medium.com/@marcoscedenillabonet/full-data-science-project-part-3-storage-architecture-with-mongodb-and-neo4j-a8ce87a4535a#:~:text=The%20combination%20of%20MongoDB,dataset%20of%20scientific%20articles)
32. **scGRN: a comprehensive single-cell gene regulatory network ...**. [https://academic.oup.com](https://academic.oup.com/nar/article/52/D1/D293/7331011#:~:text=There%20are%20few%20databases,and%20we%20noted%20that)
33. **Deep Dive: MongoDB vs Neo4j vs RDBMS — A Technical ...**. [https://medium.com](https://medium.com/@prem.shah_15628/deep-dive-mongodb-vs-neo4j-vs-rdbms-a-technical-analysis-for-complex-biological-networks-e704df639e24#:~:text=Selection%20of%20database%20systems,networks%20should%20be%20guided)
34. **Virtual Cells: Predict, Explain, Discover**. [https://arxiv.org](https://arxiv.org/html/2505.14613v3#:~:text=1.1%20The%20Predict%2DExplain%2DDiscover%20capabilities%20of%20virtual%20models)
35. **scCross: a deep generative model for unifying single-cell multi ...**. [https://genomebiology.biomedcentral.com](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-024-03338-z#:~:text=Single%2Dcell%20multi%2Domics%20data%20reveal,into%20cellular%20dynamics%20and)
36. **Stein Aerts Lab - VIB - KULeuven**. [https://aertslab.org](https://aertslab.org/#:~:text=We%20used%20single%2Dcell%20multiome,accessibility%20and%20gene%20expression)
37. **Virtual Cells: Predict, Explain, Discover**. [https://arxiv.org](https://arxiv.org/html/2505.14613v3#:~:text=automated%20labs%20for%20high%2Dthroughput%20cellular%20data%20generation%2C)
38. **Arc Institute Initiates Groundbreaking “Virtual Cell ...**. [https://bioengineer.org](https://bioengineer.org/arc-institute-initiates-groundbreaking-virtual-cell-competition-harnessing-ai-to-tackle-major-biological-challenges/#:~:text=Furthermore%2C%20the%20Virtual%20Cell,nascent%20field%20of%20virtual)
---

:::{tip}Human generated slop
The following slop has been generated by a  human being.
:::

# Wow! That's amazing.
Okay so I definitely need to dive deeper into the [Arc Virtual Cell Atlas][scBaseCount] and their [paper][scbase-paper]. `scBaseCount` sounds like something I was planning on doing myself as part of the project specs so I might as well read about how they're doing it.


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



# Another link dump

:::{danger} AI generated
The following is AI generated. Caveat lector!
:::

# Query:
> Can you give me a rundown of the latest and greatest articles, software resources, databases, and experimental methods fueling innovation in computational and experimental developmental systems biology? Specific focus on single cell methods and spatial omics tools/papers/methods would be incredibly useful. I am trying to get up to speed and it just seems like a good query to run periodically.  
> Top 10 of each. Articles. Methods. Software/databases.

# Latest Innovations in Computational and Experimental Developmental Systems Biology  
**With a Focus on Single-Cell and Spatial Omics**

This comprehensive rundown covers the top recent articles, experimental methods, and software/databases fueling innovation in developmental systems biology, with a particular emphasis on single-cell and spatial omics. The field is rapidly evolving, so this list is designed to help you get up to speed and can serve as a template for periodic updates.

---

## Top 10 Breakthrough Articles (2022–2025)

While a definitive, ranked "top 10" requires citation analysis and field consensus, the following themes and article types have dominated high-impact journals and preprint servers:

1. **Integration of Multi-Omics Data in Developmental Systems**  
   - Articles describing computational frameworks for integrating transcriptomic, epigenomic, and proteomic data at single-cell resolution, often across developmental time courses [[1]](https://www.iomcworld.com/scholarly/cell-and-developmental-biology-journals-articles-ppts-list-603.html#:~:text=%26%20Cellular%20Immunology%2C%20Developmental,in%20Developmental%20Biology%2C%20BMC).

2. **Spatial Transcriptomics in Embryogenesis**  
   - Landmark studies mapping gene expression in situ during early development using spatial transcriptomics (e.g., seqFISH+, MERFISH) [[2]](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=spatial%20resolution%2C%20multiplexing%20capability%2C,analysis%20tools%20to%20provide).

3. **Single-Cell Atlases of Model Organisms**  
   - Comprehensive single-cell atlases for zebrafish, mouse, and human embryos, revealing lineage trajectories and cell fate decisions [[3]](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=cell%2Dcell%20communication%20and%20utilized,studies%20of%20the%20heart).

4. **Organoid and Organ-on-Chip Systems**  
   - Reports on the use of organoids and microfluidic systems to model developmental processes and tissue morphogenesis [[4]](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1625942/full#:~:text=the%20broad%20reach%20of%20Cell%20and%20Developmental).

5. **Machine Learning for Cell Fate Prediction**  
   - Articles introducing machine learning models that predict cell fate transitions from single-cell multi-omics data [[5]](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=parallel%20or%20even%20the,We%20discuss%20the%20advancements).

6. **Spatial Multi-Omics in Tissue Patterning**  
   - Studies combining spatial transcriptomics with proteomics or metabolomics to dissect tissue patterning and morphogen gradients [[6]](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=Spatial%20multi%2Domic%20studies%20have,even%20the%20same%20tissue).

7. **CRISPR Screens in Developmental Contexts**  
   - High-throughput CRISPR-based perturbation screens in developing tissues, analyzed at single-cell resolution [[7]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5077642/#:~:text=Modern%20research%20tools%20are,we%20predict%20that%20an).

8. **Comparative Developmental Omics Across Species**  
   - Cross-species single-cell and spatial omics studies revealing conserved and divergent developmental programs [[8]](https://www.nature.com/articles/s42003-023-05458-x#:~:text=Today%2C%20advanced%20molecular%20tools,The%20continuous%20increase%20of).

9. **Cell-Cell Communication Networks**  
   - Articles mapping ligand-receptor interactions and signaling networks in developing tissues using spatially resolved data [[9]](https://chanzuckerberg.com/science/programs-resources/cell-science/data-insights/#:~:text=This%20project%20will%20develop,of%20a%20tissue%20of).

10. **Emerging Model Organisms and Genomic Tools**  
    - Reports on the development of genomic resources and single-cell methods for non-traditional model organisms [[7]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5077642/#:~:text=Modern%20research%20tools%20are,we%20predict%20that%20an).

*Note: For the most current articles, regularly monitor preprint servers like bioRxiv and arXiv, and set up alerts for journals such as Nature, Science, Cell, Developmental Cell, and Annual Review of Cell and Developmental Biology [[10]](https://openscience.eu/article/infrastructure/preprint-servers-story-continues#:~:text=share%20their%20work%20with,platform%20for%20rapid%20dissemination).*

---

## Top 10 Experimental Methods and Protocols

1. **MERFISH (Multiplexed Error-Robust Fluorescence In Situ Hybridization)**  
   - Enables highly multiplexed, quantitative spatial transcriptomics at subcellular resolution [[11]](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=In%20general%2C%20the%20probe%2Dbased,Some%20probe%2Dbased%20methods%20can).

2. **seqFISH+ (Sequential Fluorescence In Situ Hybridization Plus)**  
   - Allows profiling of thousands of genes in situ using advanced barcoding strategies [[11]](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=In%20general%2C%20the%20probe%2Dbased,Some%20probe%2Dbased%20methods%20can).

3. **Cyclic Immunofluorescence (CyCIF)**  
   - Multiplexed protein imaging for spatial proteomics in tissue sections [[12]](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=Targeted%20spatial%20omics%20methods,such%20as%20endogenous%20transcripts).

4. **IBEX (Iterative Bleaching Extends Multiplexity)**  
   - High-plex imaging of proteins and nucleic acids in tissues [[12]](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=Targeted%20spatial%20omics%20methods,such%20as%20endogenous%20transcripts).

5. **Spatial Multi-Omics (Joint Transcriptome, Proteome, Epigenome Profiling)**  
   - Protocols for simultaneous measurement of multiple omics layers in the same tissue section [[6]](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=Spatial%20multi%2Domic%20studies%20have,even%20the%20same%20tissue).

6. **Single-Cell Multi-Omics (scRNA-seq + ATAC-seq, etc.)**  
   - Methods for joint profiling of transcriptome and chromatin accessibility in single cells [[5]](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=parallel%20or%20even%20the,We%20discuss%20the%20advancements).

7. **CRISPR/Cas9 and RNAi in Emerging Model Organisms**  
   - Adaptation of gene editing and knockdown protocols for non-traditional models [[7]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5077642/#:~:text=Modern%20research%20tools%20are,we%20predict%20that%20an).

8. **Organoid and Organ-on-Chip Systems**  
   - Protocols for generating and analyzing 3D tissue models of development [[4]](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1625942/full#:~:text=the%20broad%20reach%20of%20Cell%20and%20Developmental).

9. **Live Imaging with High-Resolution Microscopy**  
   - Advanced imaging protocols for tracking cell behavior and lineage in vivo [[2]](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=spatial%20resolution%2C%20multiplexing%20capability%2C,analysis%20tools%20to%20provide).

10. **Probe-Based Multiplexed Imaging (e.g., MELC)**  
    - Multi-epitope ligand cartography for high-content spatial protein mapping [[12]](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=Targeted%20spatial%20omics%20methods,such%20as%20endogenous%20transcripts).

---

## Top 10 Software Resources and Databases

1. **SEEK Platform**  
   - Open-source platform for managing, sharing, and exploring systems biology data and models [[13]](https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-015-0174-y#:~:text=The%20SEEK%20is%20a,an%20access%2Dcontrolled%2C%20web%2Dbased%20environment).

2. **BioUML**  
   - Web-based platform for visual modeling, simulation, and analysis of biological systems [[14]](https://academic.oup.com/nar/article/50/W1/W124/6583230#:~:text=BioUML%20%28https%3A//www.biouml.org%29%E2%80%94is%20a%20web%2Dbased,It%20supports%20visual%20modelling).

3. **Graph Databases for Systems Biology**  
   - Tools for integrating and visualizing complex biological networks and relationships [[15]](https://academic.oup.com/bib/article/25/6/bbae561/7905378).

4. **VirtualPlant**  
   - Integrates multiple data sources for systems-level plant biology research [[16]](https://pmc.ncbi.nlm.nih.gov/articles/PMC2815851/#:~:text=The%20goal%20of%20our,access%20to%20a%20database).

5. **MAGNet**  
   - Web-enabled platform integrating bioinformatics tools for systems biology [[MAGNet]].

6. **de.NBI-SysBio Services (SABIO-RK, Excemplify, SEEK)**  
   - Suite of tools for data management and enrichment in systems biology [[de.NBI]].

7. **SIMO (Spatial Integration of Multi-Omics)**  
   - Computational tool for probabilistic alignment and integration of spatial multi-omics datasets [[17]](https://www.nature.com/articles/s41467-025-56523-4#:~:text=Technical%20limitations%20in%20spatial,Multi%2DOmics%20datasets%20through%20probabilistic).

8. **Human Cell Atlas & HuBMAP**  
   - Large-scale databases providing single-cell and spatial omics maps of human tissues [[3]](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=cell%2Dcell%20communication%20and%20utilized,studies%20of%20the%20heart).

9. **Preprint Servers (bioRxiv, arXiv)**  
   - Essential for tracking the latest computational tools, methods, and protocols [[10]](https://openscience.eu/article/infrastructure/preprint-servers-story-continues#:~:text=share%20their%20work%20with,platform%20for%20rapid%20dissemination).

10. **Model Organism Databases (MODs)**  
    - Organism-specific databases hosting genomic and functional data, with tools for querying and visualization [[18]](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-016-0276-z#:~:text=Model%20organism%20databases%20%28MODs%29,and%20provide%20query%20and).

---

## Top 10 Computational Methods for Single-Cell and Spatial Omics

1. **SIMO**  
   - Integrates spatial and non-spatial single-cell omics data using probabilistic alignment [[17]](https://www.nature.com/articles/s41467-025-56523-4#:~:text=Technical%20limitations%20in%20spatial,Multi%2DOmics%20datasets%20through%20probabilistic).

2. **Graph-Linked Embedding**  
   - Integrates single-cell data modalities at atlas scale by modeling regulatory interactions [[19]](https://www.nature.com/articles/s41587-022-01284-4#:~:text=Nature%20Biotechnology%20%2D%20Different,atlas%2Dscale%20by%20modeling%20regulatory).

3. **Weakly Linked Features Integration**  
   - Integrates spatial and single-cell data across modalities using weakly linked features [[19]](https://www.nature.com/articles/s41587-022-01284-4#:~:text=Nature%20Biotechnology%20%2D%20Different,atlas%2Dscale%20by%20modeling%20regulatory).

4. **Machine Learning for Multi-Omics Integration**  
   - AI-driven approaches for pattern recognition and cell fate prediction in developmental datasets [[5]](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=parallel%20or%20even%20the,We%20discuss%20the%20advancements).

5. **Spatial Context-Aware Cell-Cell Communication Analysis**  
   - Algorithms for inferring signaling networks from spatially resolved omics data [[9]](https://chanzuckerberg.com/science/programs-resources/cell-science/data-insights/#:~:text=This%20project%20will%20develop,of%20a%20tissue%20of).

6. **Early, Intermediate, and Late Data Integration Strategies**  
   - Computational frameworks for combining multi-omics data at different stages of analysis [[20]](https://www.sciencedirect.com/science/article/pii/S2001037021001720#:~:text=In%20this%20review%2C%20we,intermediate%2C%20and%20late%20data).

7. **Atlas-Scale Data Integration**  
   - Methods for integrating and harmonizing data across large-scale single-cell atlases [[19]](https://www.nature.com/articles/s41587-022-01284-4#:~:text=Nature%20Biotechnology%20%2D%20Different,atlas%2Dscale%20by%20modeling%20regulatory).

8. **Spatial Multi-Omics Data Analysis Pipelines**  
   - End-to-end pipelines for joint analysis of transcriptome, proteome, and epigenome in spatial context [[6]](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=Spatial%20multi%2Domic%20studies%20have,even%20the%20same%20tissue).

9. **Organoid and Tissue Simulation Platforms**  
   - Computational models for simulating organoid development and tissue morphogenesis [[4]](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1625942/full#:~:text=the%20broad%20reach%20of%20Cell%20and%20Developmental).

10. **Cross-Species Omics Integration**  
    - Methods for comparative analysis of developmental programs across model organisms [[8]](https://www.nature.com/articles/s42003-023-05458-x#:~:text=Today%2C%20advanced%20molecular%20tools,The%20continuous%20increase%20of).

---

## How to Stay Up-to-Date

- **Monitor Preprint Servers:** Set up alerts on bioRxiv and arXiv for keywords like "single-cell," "spatial omics," "developmental systems biology," and "multi-omics" [[10]](https://openscience.eu/article/infrastructure/preprint-servers-story-continues#:~:text=share%20their%20work%20with,platform%20for%20rapid%20dissemination).
- **Follow Major Journals:** Regularly check journals such as Nature, Science, Cell, Developmental Cell, and Annual Review of Cell and Developmental Biology for reviews and breakthrough articles [[1]](https://www.iomcworld.com/scholarly/cell-and-developmental-biology-journals-articles-ppts-list-603.html#:~:text=%26%20Cellular%20Immunology%2C%20Developmental,in%20Developmental%20Biology%2C%20BMC).
- **Engage with Databases:** Explore and contribute to community databases and platforms like SEEK, Human Cell Atlas, and model organism databases [[13]](https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-015-0174-y#:~:text=The%20SEEK%20is%20a,an%20access%2Dcontrolled%2C%20web%2Dbased%20environment) [[3]](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=cell%2Dcell%20communication%20and%20utilized,studies%20of%20the%20heart).
- **Attend Conferences:** Participate in conferences and workshops focused on single-cell and spatial omics technologies.

---

## Summary Table

| Category         | Top Resources/Methods/Articles (2022–2025)                                                                 |
|------------------|------------------------------------------------------------------------------------------------------------|
| Articles         | Multi-omics integration, spatial transcriptomics, single-cell atlases, organoids, ML for cell fate, etc.    |
| Methods          | MERFISH, seqFISH+, CyCIF, IBEX, spatial multi-omics, scRNA-seq+ATAC-seq, CRISPR, organoids, live imaging   |
| Software/DBs     | SEEK, BioUML, graph DBs, VirtualPlant, MAGNet, de.NBI-SysBio, SIMO, Human Cell Atlas, bioRxiv, MODs        |
| Computational    | SIMO, graph-linked embedding, weakly linked features, ML integration, spatial context-aware analysis, etc.  |

---




### Links

1. **Cell and Developmental Biology | List of High Impact Articles**. [https://www.iomcworld.com](https://www.iomcworld.com/scholarly/cell-and-developmental-biology-journals-articles-ppts-list-603.html#:~:text=%26%20Cellular%20Immunology%2C%20Developmental,in%20Developmental%20Biology%2C%20BMC)
2. **Editorial: 10 years of Frontiers in cell and developmental ...**. [https://www.frontiersin.org](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1625942/full#:~:text=the%20broad%20reach%20of%20Cell%20and%20Developmental)
3. **Editorial: 10 years of Frontiers in cell and developmental ...**. [https://www.frontiersin.org](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2025.1625942/full#:~:text=and%20treating%20complex%20biological,These%20include%20integrating%20multi%2Domics)
4. **The Future of Cell Biology: Emerging Model Organisms**. [https://pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC5077642/#:~:text=Modern%20research%20tools%20are,we%20predict%20that%20an)
5. **Model organism databases: essential resources that need the ...**. [https://bmcbiol.biomedcentral.com](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-016-0276-z#:~:text=Model%20organism%20databases%20%28MODs%29,and%20provide%20query%20and)
6. **Diversifying the concept of model organisms in the age of**. [https://www.nature.com](https://www.nature.com/articles/s42003-023-05458-x)
7. **SEEK: a systems biology data and model management platform**. [https://bmcsystbiol.biomedcentral.com](https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-015-0174-y#:~:text=The%20SEEK%20is%20a,an%20access%2Dcontrolled%2C%20web%2Dbased%20environment)
8. **BioUML—towards a universal research platform**. [https://academic.oup.com](https://academic.oup.com/nar/article/50/W1/W124/6583230#:~:text=BioUML%20%28https%3A//www.biouml.org%29%E2%80%94is%20a%20web%2Dbased,It%20supports%20visual%20modelling)
9. **Graph databases in systems biology: a systematic review**. [https://academic.oup.com](https://academic.oup.com/bib/article/25/6/bbae561/7905378)
10. **A Software Platform to Support Systems Biology Research**. [https://pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC2815851/#:~:text=The%20goal%20of%20our,access%20to%20a%20database)
11. **Spatial integration of multi-omics single-cell data with SIMO**. [https://www.nature.com](https://www.nature.com/articles/s41467-025-56523-4#:~:text=Technical%20limitations%20in%20spatial,Multi%2DOmics%20datasets%20through%20probabilistic)
12. **Multi-omics single-cell data integration and regulatory inference with graph-linked embedding | Nature Biotechnology**. [https://www.nature.com](https://www.nature.com/articles/s41587-022-01284-4#:~:text=Nature%20Biotechnology%20%2D%20Different,atlas%2Dscale%20by%20modeling%20regulatory)
13. **Spatial multi-omics: novel tools to study the complexity of ...**. [https://genomemedicine.biomedcentral.com](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=Spatial%20multi%2Domic%20studies%20have,even%20the%20same%20tissue)
14. **Computational strategies for single-cell multi-omics integration - ScienceDirect**. [https://www.sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S2001037021001720#:~:text=In%20this%20review%2C%20we,intermediate%2C%20and%20late%20data)
15. **Spatial multi-omics: novel tools to study the complexity of ...**. [https://genomemedicine.biomedcentral.com](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=parallel%20or%20even%20the,We%20discuss%20the%20advancements)
16. **Spatial integration of multi-omics single-cell data with SIMO**. [https://www.nature.com](https://www.nature.com/articles/s41467-025-56523-4#:~:text=We%20introduce%20SIMO%2C%20a,RNA%2C%20ATAC%2C%20and%20DNA)
17. **Spatial multi-omics: novel tools to study the complexity of ...**. [https://genomemedicine.biomedcentral.com](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01282-y#:~:text=cell%2Dcell%20communication%20and%20utilized,studies%20of%20the%20heart)
18. **Single-Cell Biology Data Insights Projects Grantees - CZI**. [https://chanzuckerberg.com](https://chanzuckerberg.com/science/programs-resources/cell-science/data-insights/#:~:text=This%20project%20will%20develop,of%20a%20tissue%20of)
19. **Preprint servers: The Story Continues**. [https://openscience.eu](https://openscience.eu/article/infrastructure/preprint-servers-story-continues#:~:text=share%20their%20work%20with,platform%20for%20rapid%20dissemination)
20. **Preprint servers: The Story Continues**. [https://openscience.eu](https://openscience.eu/article/infrastructure/preprint-servers-story-continues#:~:text=in%20the%20field%20of,the%20global%20scientific%20community)
21. **Preprints in the Spotlight**. [https://sr.ithaka.org](https://sr.ithaka.org/publications/preprints-in-the-spotlight/#:~:text=published%20in%202018.%5B14%5D%20While,total%20number%20of%20papers)
22. **Are preprints the future of research?**. [https://ideas.newsrx.com](https://ideas.newsrx.com/are-preprints-the-future-of-research#:~:text=Preprints%20nevertheless%20can%20fulfill,challenges%20facing%20science%20in)
23. **Spatial omics technologies at multimodal and single cell ...**. [https://genomebiology.biomedcentral.com](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=spatial%20resolution%2C%20multiplexing%20capability%2C,analysis%20tools%20to%20provide)
24. **Spatial omics technologies at multimodal and single cell ...**. [https://genomebiology.biomedcentral.com](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=Targeted%20spatial%20omics%20methods,such%20as%20endogenous%20transcripts)
25. **Spatial omics technologies at multimodal and single cell ...**. [https://genomebiology.biomedcentral.com](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02824-6#:~:text=In%20general%2C%20the%20probe%2Dbased,Some%20probe%2Dbased%20methods%20can)




[scBaseCount]: https://github.com/ArcInstitute/arc-virtual-cell-atlas/blob/main/scBaseCount/README.md
[GRiNS]: https://github.com/MoltenEcdysone09/GRiNS/blob/main/README.md
[you-epiwad]: https://you.com/projects/686184e2a9811bf5aada25c7
[scbase-paper]: https://www.biorxiv.org/content/10.1101/2025.02.27.640494v2