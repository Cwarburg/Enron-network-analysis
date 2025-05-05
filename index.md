---
layout: default
title: Enron Email Network Analysis
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
  margin-bottom: 1rem;
  font-weight: 800;
}

h2 {
  color: var(--secondary-color);
  margin-top: 3rem;
  font-weight: 700;
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


## Overview
This project analyzes the communication network within Enron Corporation using email data. The analysis focuses on identifying key employees and understanding their communication patterns. The motivation behind this project

## Network Visualization
![Enron Email Network](images/networkgraph.png.png)

The network visualization shows the communication patterns between Enron employees. Each node represents an employee, and each edge represents an email communication. The visualization highlights the most active communicators in the network.

## Key Findings

### Most Central Communicators
The following employees were identified as the most central in the communication network:

1. [Top Central Person 1]
2. [Top Central Person 2]
3. [Top Central Person 3]
4. [Top Central Person 4]
5. [Top Central Person 5]

### Network Statistics
<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-number">[Number]</div>
    <div>Total Employees</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">[Number]</div>
    <div>Email Connections</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">[Number]</div>
    <div>Avg. Connections</div>
  </div>
</div>

## Methodology
The analysis was conducted using:
<div class="methodology">
  <span class="methodology-item">Python</span>
  <span class="methodology-item">NetworkX</span>
  <span class="methodology-item">Pandas</span>
  <span class="methodology-item">Matplotlib</span>
</div>

The network was filtered to include only:
- Enron email addresses (@enron.com)
- Employees who sent more than 50 emails

## Data Source
The analysis is based on the Enron email dataset, which contains internal communications from Enron Corporation.

## Code
The analysis code is available in the [GitHub repository](https://github.com/yourusername/enron-network-analysis).

<div class="contact-section">
  <h2>Contact</h2>
  <p>For questions or comments about this analysis, please contact [your email].</p>
</div>