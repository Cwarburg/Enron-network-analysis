---
layout: default
title: "Enron Network Analysis"
subtitle: "Exploring the Enron dataset with Natural Language Processing"
---

<style>
:root {
  --primary-color: #2c3e50;
  --secondary-color: #3498db;
  --accent-color: #e74c3c;
  --text-color: #2c3e50;
  --light-bg: #f8f9fa;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

header {
  text-align: center;
  margin-bottom: 4rem;
  padding: 2rem 0;
  border-bottom: 2px solid var(--light-bg);
}

h1 {
  font-size: 3rem;
  color: var(--primary-color);
  margin-bottom: 0.5rem;
  font-weight: 800;
}

.subtitle {
  font-size: 1.5rem;
  color: var(--secondary-color);
  font-style: italic;
  margin-top: -0.5rem;
}

h2 {
  color: var(--secondary-color);
  margin-top: 3rem;
  font-weight: 700;
}

h3 {
  color: var(--accent-color);
  margin-top: 2rem;
  font-weight: 700;
}

.network-visualization img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}

.network-visualization {
  width: 100%;
  max-width: 800px;
  margin: 2rem auto;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.network-visualization:hover {
  transform: scale(1.02);
}

.key-findings {
  background: var(--light-bg);
  padding: 2rem;
  border-radius: 12px;
  margin: 2rem 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  text-align: center;
  transition: transform 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--secondary-color);
  margin-bottom: 0.5rem;
}

.methodology {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin: 1rem 0;
}

.methodology-item {
  background: var(--secondary-color);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.9rem;
}

.contact-section {
  text-align: center;
  margin-top: 4rem;
  padding: 2rem;
  background: var(--light-bg);
  border-radius: 12px;
}

@media (max-width: 768px) {
  body {
    padding: 1rem;
  }
  
  h1 {
    font-size: 2rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<header>
  <h1>Enron Network Analysis</h1>
  <p class="subtitle">Exploring the Enron dataset with Natural Language Processing</p>
</header>

## Introduction

The Enron Email Dataset contains roughly half a million messages exchanged among some 6,000 employees—mostly senior executives—between 1998 and 2002. Originally released during the FERC inquiry into Enron’s collapse, it offers an unparalleled glimpse into the everyday communications and decision-making of a major corporation at a pivotal moment in history.

In this project, we focus on the subset of 150 executive-level employees, transforming their email traffic into a directed social network. By examining this network’s structure and evolution, we aim to surface communication patterns that might signal emerging crises. We then layer in Natural Language Processing—tracking sentiment and topic shifts over time—to explore whether early warning signs of malfeasance can be detected before it’s too late.


---

## Network Analysis

<figure class="network-visualization">
  <img src="images/completenetwork.png" alt="Graph of the complete network of all executives" style="max-width: 100%; height: auto;">
  <figcaption>Figure 1. Graph of the complete network of all executives.</figcaption>
</figure>

*Figure 1. Graph of the complete network of all executives.*



<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-number">140</div>
    <div>Active Employees</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">16000</div>
    <div>Emails</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">18.93</div>
    <div>Average Degree</div>
  </div>
</div>
To uncover the key players and structural dynamics within Enron’s executive communication network, we apply three complementary techniques:

1. **Centrality Measures**  
   - **Eigenvector Centrality** identifies nodes connected to other highly influential nodes, highlighting executives whose reach extends through the network’s most powerful hubs.  
   - **Degree Centrality** (in- and out-degree) reveals who sends the most messages and who receives the most, offering a quantitative measure of activity and visibility.  

2. **Betweenness Centrality**  
   Betweenness quantifies how often a node lies on the shortest paths between pairs of others. High-betweenness individuals serve as “bridges” or information bottlenecks—critically positioned to control the flow of knowledge or to detect and potentially obscure sensitive topics.

3. **Community Detection**  
   By partitioning the network into tightly connected groups (or communities), we can spot clusters of executives who communicate more frequently among themselves than with the broader organization. This helps us identify functional teams, informal cliques, or potentially siloed groups that may harbor distinct conversational norms or secretive exchanges.

Together, these methods allow us to pinpoint not only the most influential or active individuals but also the structural gateways and subgroups that shape information flow—and potentially conceal it—within Enron’s executive ranks.  


### Centrality Scores

Below we compare the top 5 nodes by **degree centrality** and **eigenvector centrality** side by side to highlight the most connected and most influential communicators.

### Centrality Scores

| **Degree Centrality** | **Eigenvector Centrality** |
| ---------------------- | -------------------------- |
| <img src="images/degreecentrality.png" alt="Degree Centrality" style="width: 300px;">  
  *Figure 1. Top 5 Degree Centrality Scores.* | <img src="images/eigencentrality.png" alt="Eigenvector Centrality" style="width: 300px;">  
  *Figure 2. Top 5 Eigenvector Centrality Scores.* |


### Betweenness Score

Betweenness centrality shows which employees act as bridges on the shortest paths between others—key for detecting information bottlenecks.

<figure class="network-visualization">
  <img src="images/betweenness.png" alt="Betweenness centrality in the Enron network" style="max-width: 100%; height: auto;">
  <figcaption>Figure Y. Nodes with highest betweenness.</figcaption>
</figure>

### Community Detection

Using the Louvain algorithm, we identified six distinct communities in the Enron executive network. The node with the highest degree centrality was John Lavorato, Enron’s COO. Intriguingly, his community also included Kenneth Lay and Jeffrey Skilling—both of whom were later convicted of fraud and insider trading and served prison sentences.



---

## Further Investigation and NLP

In this part, we want to determine if the the sentiment of Kenneth Lay and J. Skilling’s changed during the collapse of enron.

---



## Data Sources

The dataset can be downloaded from [Kaggle](https://www.kaggle.com/datasets/rcmonteiro/structured-enron-dataset/data).

## Contact

<div class="contact-section">
  <h2>Contact</h2>
  <p>This project was made by Christian Warburg (s225083) and Sofus Carstens (s22…) for the Computational Social Science course.</p>
</div>
