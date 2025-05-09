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

Below we compare the top 5 nodes by **degree** and **eigenvector** centralities side by side.

<table>
  <tr>
    <td align="center" valign="top">
      <figure>
        <img src="images/degreecentrality.png" alt="Degree Centrality" width="300"><br>
        <figcaption><em>Figure 2.</em> Top 5 Degree Centrality Scores.</figcaption>
      </figure>
    </td>
    <td align="center" valign="top">
      <figure>
        <img src="images/eigencentrality.png" alt="Eigenvector Centrality" width="300"><br>
        <figcaption><em>Figure 3.</em> Top 5 Eigenvector Centrality Scores.</figcaption>
      </figure>
    </td>
  </tr>
</table>

#### Sub‐section: Centrality Insights

Both charts highlight **kitchen-l** and **lavorato-j** as the network’s primary hubs—high‐volume communicators whose partners are also highly connected. The swap between **ward-k** (high message count) and **whalley-g** (strategically influential ties) in the fourth spot illustrates that sheer activity (degree) doesn’t always equate to influence (eigenvector). Overall, combining these measures reveals both the busiest and the most impactful actors in Enron’s executive email network.



### Betweenness Score

Betweenness centrality shows which employees act as bridges on the shortest paths between others—key for detecting information bottlenecks.

<figure class="network-visualization" style="max-width: 600px; margin: 2rem auto;">
  <img src="images/betweenness.png" alt="Betweenness centrality in the Enron network" style="width: 100%; height: auto;">
  <figcaption>Figure 4. Nodes with highest betweenness.</figcaption>
</figure>

#### Betweenness Centrality Insights

The betweenness chart highlights **ward-k** as the primary “bridge” in the network—positioned on the most shortest paths between executives. Following him, **grigsby-m**, **dasovich-j**, **presto-k**, and **scott-s** also serve as key intermediaries. These individuals are crucial for information flow, acting as gatekeepers who connect otherwise distant clusters within Enron’s executive communications.  


### Community Detection

Using the Louvain algorithm, we identified six distinct communities in the Enron executive network. The node with the highest degree centrality was John Lavorato, Enron’s COO. Intriguingly, his community also included [Kenneth Lay ](https://en.wikipedia.org/wiki/Kenneth_Lay )and [Jeffrey Skilling](https://en.wikipedia.org/wiki/Jeffrey_Skilling)—both of whom were later convicted of fraud and insider trading and served prison sentences.
<figure class="network-visualization" style="max-width: 600px; margin: 2rem auto;">
  <img src="images/community2.png" alt="Visualization of community 2" style="width: 100%; height: auto;">
  <figcaption>Figure 4. Nodes with highest betweenness.</figcaption>
</figure>

---

## Further Investigation and NLP

In this part, we want to determine if the sentiment of Kenneth Lay and J. Skilling’s emails changed during the collapse of Enron.

---

## Sentiment Analysis Over Time

Sentiment analysis is the process of automatically determining whether a piece of text expresses a positive, negative, or neutral attitude. By scoring the emotional tone of written language, it lets us quantify how people feel—whether they’re upbeat, anxious, or somewhere in between. For our Enron project, we used a **lexicon-based** approach via **TextBlob’s polarity analyzer**:

1. **Word-level scoring**: Each word in an email is looked up in a built-in dictionary that assigns it a small positive or negative weight.
2. **Message polarity**: Those word scores are averaged and normalized into a single polarity value between –1.0 (very negative) and +1.0 (very positive).

By using this **lexicon-based** approach, no training data is needed and it gives a clear, continuous measure of tone that we can track over time.

In the network analysis phase, we computed betweenness centrality for every employee (node) in the Enron executive‐email graph. For this natural language processing part of the analysis we focus on the **10 highest betweenness** individuals. We call these individuals our **top hubs**. By focusing only on the top hubs, we focus on the most strategic information brokers. Tracking sentiment on Enron's key decision makers and gatekeepers outgoing mail only, filtering out background noise of the entire employee base. 


<figure class="network-visualization">
  <img src="images/sentimentovertime.png" alt="Average sentiment of top hubs over time" style="max-width: 100%; height: auto;">
  <figcaption>Figure 8. Average monthly sentiment polarity for top betweenness hubs (Dec 1999–Apr 2002).</figcaption>
</figure>

We see on the plot that the overall trend is positive (score > 0). This could be due to the **corporate tone bias**. Executive email tends to skew polite, upbeat, and solution-oriented. Even bad news is couched in neutral or euphemistic language (“we’ll need to revisit these numbers” rather than “this is a disaster”), so polarity scores rarely plunge far below zero. In reality a sentiment polarity score of 0.05 to 0.15 is in the lower end for a company.

Although Enron filed for bankruptcy on December 2, 2001, our monthly averages don’t show a steady decline beforehand because top executives were still using controlled, neutral‐to‐positive corporate language in their internal emails—focusing on damage control and jargon rather than panic—and any isolated “worried” messages were smoothed out when averaged over hundreds of monthly communications. The decline from 2002-02 to 2002-03 is due to suffcient amount of emails in march 2002.


---



## Data Sources

The dataset can be downloaded from [Kaggle](https://www.kaggle.com/datasets/rcmonteiro/structured-enron-dataset/data).
Our [github](https://github.com/Cwarburg/Enron-network-analysis/tree/main/images)

## Contact

<div class="contact-section">
  <h2>Contact</h2>
  <p>This project was made by Christian Warburg (s225083) and Sofus Carstens (s224959) for the Computational Social Science course.</p>
</div>
