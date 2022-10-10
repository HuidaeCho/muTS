# µTS
Microscopic Traffic Simulator (µTS)

## An open-source microscopic traffic simulator (µTS) using probabilistic estimation of vehicle behaviors

Emma Vail, Huidae Cho

As highway infrastructure and environmental land use take priority, traffic simulation and forecasting have become increasingly important. Experimentation with numerous road network systems and traffic data acquisition using sensors and other physical methods is typically costly whereas simulation technologies have paved the way for easier and more affordable traffic research. The objective of this project is to model a functioning microscopic traffic simulation that is capable of representing variations in traffic volume, patterns, and time. In this research, we will utilize various probability distributions to estimate different parameters related to vehicle behaviors. Microscopic vehicles will all maintain velocities that follow the normal distribution and their arrival and departure rates at a monitoring site will be modeled using the Poisson distribution. We will take an open-source approach using Python modules including OSGeo, NumPy, Matplotlib, etc., for microscopic traffic simulation. This research is relevant and significant in that one should be able to pair the simulation code with data and extensive outside research in order to better establish reliable predictions. For example, the code can be implemented with real-world traffic data to predict carbon emissions produced from different types of vehicles. We will present our final product called the Microscopic Traffic Simulator (µTS), which will consist of interactive Python code with the ability to predict traffic variability that can be used alongside other research to enhance and model the results. The result will have the potential to be extended to account for specific research variables and vehicle velocities that differ from each other.

Keywords: open-source traffic simulation, probability distribution, Python

[FOSS4G 2022 abstract](https://talks.osgeo.org/foss4g-2022/talk/review/QEFTUYCHHGBZYYTYHS3K8XXLEUWUHEXK)

## Demo for 100 cars per day

![simulation.gif](simulation.gif "simulation.gif")

## References

Berry, D. S. and Belmont, D. M., 1951. Distribution of Vehicle Speeds and Travel Times. Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability (2), 589-602. [Online](https://projecteuclid.org/proceedings/berkeley-symposium-on-mathematical-statistics-and-probability/Proceedings-of-the-Second-Berkeley-Symposium-on-Mathematical-Statistics-and/Chapter/Distribution-of-Vehicle-Speeds-and-Travel-Times/bsmsp/1200500257), [PDF](https://digitalassets.lib.berkeley.edu/math/ucb/text/math_s2_article-43.pdf).

## License

Copyright (C) 2022 [Huidae Cho](https://hcho.isnew.info/)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <<https://www.gnu.org/licenses/>>.
