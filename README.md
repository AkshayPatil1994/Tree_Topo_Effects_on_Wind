# Tree_Topo_Effects_on_Wind
Repository for MSc Geomatics Thesis by R.Fu at Delft University of Technology


## Modeling tree topology effects on wind

![This is an image](https://github.com/furunnan/Tree_Topo_Effects_on_Wind/blob/main/cover.png)

Author\\
FU, RUNNAN (TU Delft Architecture and the Built Environment; TU Delft Urbanism)

Contributor\\
Garcia Sanchez, C. (mentor) \\
Pađen, I. (mentor)


## Research Abstract
Planting trees is widely considered an effective way to create a good urban wind environment, improve air quality, mitigate heat island effects, improve pedestrian wind comfort and reduce building energy consumption. To assess tree effects and find suitable tree setups in urban areas, Computational Fluid Dynamic (CFD) simulations can be used.
To handle trees in CFD simulations, the implicit tree modeling approach, i.e, the porosity model, is widely used where finite volume cells that roughly account for trees are marked as porous zones. Some studies have also attempted to model trees as obstacles rather than porous zones, which can be referred to as an explicit tree modeling approach. The difference between these two approaches deserves further study. Also, for practical purposes and lack of information, the geometric features of trees are usually oversimplified or even ignored in CFD simulations.
This thesis investigates the difference between implicit and explicit tree modeling approaches and analyzes the impact of tree Level of Detail (LoD) and shapes on the flow structure. For comparative analysis, several numerical test cases with different urban complexities, tree modeling approaches, tree LoDs, tree shapes, Leaf Area Density (LAD) values, and wind directions were used for CFD simulations.
The results show: (a) the implicit models always allow some of the wind flow into the porous cells no matter how high the LAD values are, resulting in smaller wind acceleration on the lateral sides of implicit tree models; (b) for the idealized street canyon and realistic urban geometry test cases simulated in this thesis, the velocity magnitude differences between the LoD2 cases and the LoD3 cases are rather limited, with maximum differences in the order of 0.5 m/s; (c) differences in tree shapes, LAD values, and wind directions will change the effects of tree modeling approaches and tree LoDs on wind. For instance, the case using an isolated explicit LoD2 conifer tree model has a different wake flow pattern from other explicit cases. Also, with the inflow direction perpendicular to buildings, the higher the LAD values, the larger the velocity magnitude difference between cases using LoD2 tree models and those using LoD3 tree models.

To reference this document use [this](http://resolver.tudelft.nl/uuid:557e824d-a088-4cf4-8fe5-c98f5b893057)
