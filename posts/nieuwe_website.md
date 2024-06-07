---
title: Nieuwe website opzet
date: 2024-01-01
tags: website, cloud, solution design
---


Het is altijd leuk om hobbymatig bezig te zijn om een website in elkaar te zetten. Van het inzetten van zoiets als Jekyll en auto deploying door middel van GitHub Actions voor een website die is opgebouwd met markdown bestanden en hosting op GitHub Pages tot het zelf in elkaar zetten van een Wordpress site. 

Mijn eigen website heeft al vele iteraties qua tech setup meegemaakt:  
- WYSIWYG web builder statische website  
- Verscheidene Wordpress variaties en themes  
- Markdown setups met tools als Jekyll en hosting op blob storage met CDN erop  

Tot nu een variatie waarbij een simpele blog setup is gebouwd met Python FastAPI en markdown files. Het idee is hierachter dat het altijd leuk is met nieuwe Python frameworks aan de gang te gaan. 

Verder wordt de website nu in een Docker image gezet die in een eigen private image repository wordt gezet waarna het gehost wordt op een Kubernetes cluster met een loadbalancer ervoor. Deze setup heb ik voornamelijk gekozen omdat ik toch al een cluster heb draaien bij een cloud provider voor wat andere projecten en ik zo zaken kan samenvoegen. Zo lift ik bovendien ook mee op de allernieuwste IT-hype om alles in Kubernetes te plaatsen. 