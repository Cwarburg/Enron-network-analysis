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

The Enron Email Dataset comprises approximately 500,000 emails from around 6,000 Enron employees, primarily executives, spanning 1998 to 2002. Released during the FERC investigation into Enron’s collapse, this corpus provides a unique window into corporate communications at a momentous moment in modern business history.

---

## Network Analysis

### Centrality Scores

Centrality measures quantify how “important” or well-connected a node is within the network. Here we look at degree, closeness, and eigenvector centralities to highlight the top communicators.

<figure class="network-visualization">
  <img src="images/centrality.png" alt="Centrality scores in the Enron network">
  <figcaption>Figure X. Top centrality scores.</figcaption>
</figure>

### Betweenness Score

Betweenness centrality shows which employees act as bridges on the shortest paths between others—key for detecting information bottlenecks.

<figure class="network-visualization">
  <img src="images/betweenness.png" alt="Betweenness centrality in the Enron network">
  <figcaption>Figure Y. Nodes with highest betweenness.</figcaption>
</figure>

### Community Detection

Using the Louvain method, we partitioned the network into six densely-connected clusters, reflecting functional or departmental groupings within Enron.

<figure class="network-visualization">
  <img src="images/communities.png" alt="Detected communities in the Enron network">
  <figcaption>Figure Z. Enron email communities.</figcaption>
</figure>

---

## Further Investigation

Here you can outline additional analyses (NLP topic modeling, temporal dynamics, anomaly detection, etc.) or link to interactive dashboards.

---

## Key Statistics

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
    <div class="stat-number">6</div>
    <div>Detected Communities</div>
  </div>
</div>

---

## Contact

<div class="contact-section">
  <h2>Contact</h2>
  <p>This project was made by Christian Warburg (s225083) and Sofus Carstens (s22…) for the Computational Social Science course.</p>
</div>
