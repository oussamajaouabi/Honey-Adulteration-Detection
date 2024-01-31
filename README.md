# Honey Adulteration

## Hyperspectral Imaging

- Spectroscopy : the study of light interaction with materials.
- It examines how light behaves in the target and recognizes materials based on their different spectral signatures.
- Spectrum describes the amount of light in different wavelengths.
  
![image](https://github.com/oussamajaouabi/Honey-Adulteration-Detection/assets/96437883/f522b1b2-2ca6-4478-bc47-276fb82683ba)

- Hyperspectral Imaging is an analytical technique based on spectroscopy. It collects hundreds of images at different wavelengths for the same spatial area.
- Each material possesses a specific spectral signature that can be employed as a ‘fingerprint’ for its unique identification.

![image](https://github.com/oussamajaouabi/Honey-Adulteration-Detection/assets/96437883/e339b189-68c5-4eb4-877a-273ec6d4cb33)

- Hyperspectral imaging is employed in different fields such as :
  - astronomy,
  - agriculture,
  - molecular biology,
  - biomedical imaging,
  - geology,
  - physics,
  - cultural heritage,
  - food processing,
  - environment,
  - surveillance.

- It is also used in various industrial processes, mainly to determine product quality.

Hyperspectral imaging for food fraud detection :
- Determining chemical composition: different materials have unique spectral signatures, making it possible to identify the substances.
- Indications of concentration: by analysing variation in light intensity at different wavelengths, hyperspectral imaging can provide indications of the concentration of chemical components.

## Hyperspectral Imaging adulterated honey

Tessa Phillips, Waleed Abdulla. A new honey adulteration detection approach using hyperspectral imaging and machine learning. European Food Research and Technology (2023) 249:259–272. ([link](https://doi.org/10.1007/s00217-022-04113-9))

Hyperspectral Imaging adulterated honey dataset : 

```
https://auckland.figshare.com/articles/dataset/Hyperspectral_Imaging_adulterated_honey_dataset/16441686/1

```

A new honey adulteration detection approach using hyperspectral imaging and machine learning :
- Use hyperspectral imaging and machine learning techniques to detect adulteration honey with sugar with different concentrations (5%, 10%, 25%, 50%).
- Above 95% accuracy was achieved for binary adulteration detection and multi-class classification between different adulterant concentrations.

Sample preparation and adulteration :

![image](https://github.com/oussamajaouabi/Honey-Adulteration-Detection/assets/96437883/096b4d61-3f21-43df-99df-5f43e7d79b88)


Dataset Description :

- The dataset of honey samples contains 8675 total instances.
- The dataset contains 12 different honey products from seven different brands with 11 different botanical origins labels (from New Zealand).
- It contains 128 attributes - representing the spectral wavelengths of the hyperspectral camera. These wavelengths range from 400nm to 1064nm.

Dataset Attributes

- Brand: represents the manufacturer who supplied the honey.
- Acquisition: represents the different sample images for the same type and brand of honey. Each sample is numbered from one to six to indicate the corresponding acquisition.
- Class: represents the honey class, corresponding to the botanical origin of the honey.
- Concentration/Concentration_class: represent the actual sugar concentration present in the honey sample
- 128 other Attributes corresponding to the spectral wavelengths measured.

## Demo

https://github.com/oussamajaouabi/Honey-Adulteration-Detection/assets/96437883/36505518-bfee-4c63-ae0c-59f2dcaf8639
