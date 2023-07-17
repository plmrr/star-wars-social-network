# Star Wars social network
The object of this research is the social network of characters appearing in the films of the series of'Star Wars' episodes 1 through 7 representing the interactions between characters and theirappearances in the film canon over time.

# Use of data to create a network
The dynamics characterizing the network is the appearance of new nodes, consistent with the order in which the these characters appeared in the films, and the disappearance of nodes representing these characters in the event of their case of their death. 
Along with time, connections are also added between characters, which represent the occurrence of interactions between them.

#### Note
Data don't include episodes VIII and IX.

# Main objective
The main objective was to study how, with the appearance of new characters or their deaths changes the average distance needed to transmit information between two characters. This goal was accomplished with the help of examining the change in graph diameter over time.

# Side properties of the network
Additional network properties that were examined are:
- The average number of characters connecting two characters - obtained using the average length of the of the shortest path
- The percentage of familiarity between all characters - a quantity obtained by calculating the density of the network
- The character with the highest number of interactions with other characters - the node with the highest degree
- The most isolated character - the node with the lowest degree
- Cluster of closely related characters - maximum clique
- Key character for fast flow of information - percentage of all shortest paths passing through a node
- Key familiarity between two characters for fast information flow information - percentage of all pairs of shortest paths passing through an edge

# Visualizations

### Complex network:

![new](https://github.com/plmrr/star-wars-social-network/assets/130595899/869f3538-be77-48dd-b50c-25f61bf73e41)

### Graph: 

![static_network](https://github.com/plmrr/star-wars-social-network/assets/130595899/979b7c3f-6b2d-45dc-bc05-9c5bc423b781)

# Results for static graph
- Average length of the shortest path was 2.66.
- Diameter of the static network is 6.
- Percentage of familiarity between characters was 7.37%.
- Node with the highest degree turned out to be Anakin Skywalker.
- The most isolated character is Colonel Datoo.
- The highest concentration of closely related characters includes: Anakin Skywalker, Padme Amidala, Palpatine, C-3P0, Yoda, R2-D2, and Bail Organa.
- A key figure for the rapid transfer of information is Obi-Wan Kenobi, through whom 20.8% of all shortest paths go through.
- The acquaintance through which the most shortest paths pass is the acquaintance Between C-3P0 and Poe Dameron with a score of 4.3%.

# Analysis & conclusions for complex network
- The diameter of the network, oscillating between 0 and 4, is the expected value, allowing information to spread quickly between characters.

- A low value of network density indicates the lack of interaction of most characters in the "Star Wars" film canon.

- The edge with the highest number of shortest paths through it connects C-3P0 and Poe Dameron, probably due to the character's connection to different films in the series.

- Predicted results include Anakin Skywalker as the node with the highest degree, and Obi-Wan Kenobi as the character through whom the most shortest paths pass, due to their presence in most episodes.

- Characters belonging to the maximum clique have a large number of conversations in the prequel films.

- The social network of Star Wars characters exhibits the characteristics of a scale-free network and a small-worlds network, with a hierarchical structure of connections, hubs and a low diameter.

- The small diameter of the network and the characteristics of the small-worlds network allow for the rapid flow of information and resilience to accidental glitches, but at the same time make the network vulnerable to deliberate attacks that can lead to a disjointed network and an increase in the diameter value and the average shortest path between characters

# Dataset credits: 
Evelina Gabasova. (2016). Star Wars social network (Version 1.0.1) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.1411479
