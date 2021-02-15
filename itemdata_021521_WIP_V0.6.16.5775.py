import os, json
from pathlib import Path

###Game Version EA 0.6.16.5775
###Contributor: Misaka Rin.
###Last Edited: 02/15/2021



def getitems():
    itemdict_en = {'Components' : {}, 'Buildings' : {}}
    #Speeds for items produced by assembling machines are assumed to be 1.0x (Equals to replicator speed after '''Quantum Printing Technology''' has been researched.)
    #format: 
    #{'Components/Buildings' : 
        #{'item name' : 
            #{'place' : 'Facility', 
                #'speed' : 'amountperminute', 
                #'Rep-ability' : 'True'/'False',
                #'outcome' : { '1' : ['name', 'amount1'] , etc...  }, 
                #'input material' : { '1' : ['name1', 'amount1'], etc...  } 
            #}
        #}
    #}


    #Components

    #Category I
    itemdict_en['Components']['Iron Ingot'] = {'place' : 'Smelter', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Iron Ingot', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ore', '1'] } }

    itemdict_en['Components']['Copper Ingot'] = {'place' : 'Smelter', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Copper Ingot', '1'] }, 
    'inputmaterial' :{ '1' : ['Copper Ore', '1'] } }

    itemdict_en['Components']['High-Purity Silicon'] = {'place' : 'Smelter', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['High-Purity Silicon', '1'] }, 
    'inputmaterial' :{ '1' : ['Silicon Ore', '2'] } }

    itemdict_en['Components']['Titanium Ingot'] = {'place' : 'Smelter', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Titanium Ingot', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Ore', '2'] } }

    itemdict_en['Components']['Stone Brick'] = {'place' : 'Smelter', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Stone Brick', '1'] }, 
    'inputmaterial' :{ '1' : ['Stone', '1'] } }

    itemdict_en['Components']['Enegetic Graphite'] = {'place' : 'Smelter', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Enegetic Graphite', '1'] }, 
    'inputmaterial' :{ '1' : ['Coal', '2'] } }

    itemdict_en['Components']['Recipe Plasma Refining'] = {'place' : 'Oil Refinery', 
    'speed' : '15', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Hydrogen', '1'], '2' : ['Refined Oil', '2'] }, 
    'inputmaterial' :{ '1' : ['Crude Oil', '2'] } }

    itemdict_en['Components']['Plastic'] = {'place' : 'Chemical Plant', 
    'speed' : '20', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Plastic', '1'] }, 
    'inputmaterial' :{ '1' : ['Refined Oil', '2'], '2' : ['Enegetic Graphite', '1'] } }

    itemdict_en['Components']['Graphene'] = {'place' : 'Chemical Plant', 
    'speed' : '20', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Graphene', '2'] }, 
    'inputmaterial' :{ '1' : ['Enegetic Graphite', '3'], '2' : ['Sulfuric Acid', '1'] } }

    #Category II
    itemdict_en['Components']['Magnet'] = {'place' : 'Smelter', 
    'speed' : '40', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Magnet', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ore', '1'] } }

    itemdict_en['Components']['Magnetic Coil'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Magnetic Coil', '2'] }, 
    'inputmaterial' :{ '1' : ['Magnet', '2'], '2' : ['Copper Ingot', '1'] } }

    itemdict_en['Components']['Crystal Silicon'] = {'place' : 'Smelter', 
    'speed' : '30', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Crystal Silicon', '1'] }, 
    'inputmaterial' :{ '1' : ['High-Purity Silicon', '1'] } }

    itemdict_en['Components']['Titanium Alloy'] = {'place' : 'Smelter', 
    'speed' : '5', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Titanium Alloy', '4'] }, 
    'inputmaterial' :{ '1' : ['Titanium Ingot', '4'], '2' : ['Steel', '4'], '3' : ['Sulfuric Acid', '8'] } }

    itemdict_en['Components']['Glass'] = {'place' : 'Smelter', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Glass', '1'] }, 
    'inputmaterial' :{ '1' : ['Stone', '2'] } }

    itemdict_en['Components']['Diamond'] = {'place' : 'Smelter', 
    'speed' : '30', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Diamond', '1'] }, 
    'inputmaterial' :{ '1' : ['Enegetic Graphite', '1'] } }

    itemdict_en['Components']['Recipe X-Ray Cracking'] = {'place' : 'Oil Refinery', 
    'speed' : '15', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Hydrogen', '3'], '2' : ['Enegetic Graphite', '1'] }, 
    'inputmaterial' :{ '1' : ['Refined Oil', '1'], '2' : ['Hydrogen', '2'] } }

    itemdict_en['Components']['Organic Crystal'] = {'place' : 'Chemical Plant', 
    'speed' : '10', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Organic Crystal', '1'] }, 
    'inputmaterial' :{ '1' : ['Plastic', '2'], '2' : ['Refined Oil', '1'], '3' : ['Water', '1'] } }

    itemdict_en['Components']['Recipe Graphene Advanced'] = {'place' : 'Chemical Plant', 
    'speed' : '30', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Graphene', '1'], '2' : ['Hydrogen', '1'] }, 
    'inputmaterial' :{ '1' : ['Fire Ice', '2'] } }

    itemdict_en['Components']['Hydrogen Fuel Rod'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Hydrogen Fuel Rod', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Ingot', '1'], '2' : ['Hydrogen', '5'] } }

    itemdict_en['Components']['Deuteron Fuel Rod'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Deuteron Fuel Rod', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Alloy', '1'], '2' : ['Deuteron', '10'], '3' : ['Super-Magnetic Ring', '1'] } }

    itemdict_en['Components']['Antimatter Fuel Rod'] = {'place' : 'Assembling Machine', 
    'speed' : '5', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Antimatter Fuel Rod', '1'] }, 
    'inputmaterial' :{ '1' : ['Antimatter', '10'], '2' : ['Hydrogen', '10'], '3' : ['Annihilation Constraint Sphere', '1'], '4' : ['Titanium Alloy', '1'] } }

    #Category III
    itemdict_en['Components']['Steel'] = {'place' : 'Smelter', 
    'speed' : '20', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Steel', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '3'] } }

    itemdict_en['Components']['Electric Motor'] = {'place' : 'Assembling Machine', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Electric Motor', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '2'], '2' : ['Gear', '1'], '3' : ['Magnetic Coil', '1'] } }

    itemdict_en['Components']['Recipe Crystal Silicon Advanced'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Crystal Silicon', '1'] }, 
    'inputmaterial' :{ '1' : ['Fractal Silicon', '1'] } }

    itemdict_en['Components']['Titanium Glass'] = {'place' : 'Assembling Machine', 
    'speed' : '12', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Titanium Glass', '2'] }, 
    'inputmaterial' :{ '1' : ['Glass', '2'], '2' : ['Titanium Ingot', '2'], '3' : ['Water', '2'] } }

    itemdict_en['Components']['Prism'] = {'place' : 'Assembling Machine', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Prism', '2'] }, 
    'inputmaterial' :{ '1' : ['Glass', '3'] } }

    itemdict_en['Components']['Recipe Diamond Advanced'] = {'place' : 'Smelter', 
    'speed' : '30', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Diamond', '1'] }, 
    'inputmaterial' :{ '1' : ['Kimberlite ore', '1'] } }

    itemdict_en['Components']['Recipe Deuteron Fractionation'] = {'place' : 'Fractionator', 
    'speed' : '18', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Deuterium', '1'] }, 
    'inputmaterial' :{ '1' : ['Hydrogen', '1'] } }

    itemdict_en['Components']['Recipe Organic Crystal Original'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Organic Crystal', '1'] }, 
    'inputmaterial' :{ '1' : ['Log', '20'], '2' : ['Plant Fuel', '30'], '3' : ['Water', '10']  } }

    itemdict_en['Components']['Titanium Crystal'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Titanium Crystal', '1'] }, 
    'inputmaterial' :{ '1' : ['Organic Crystal', '1'], '2' : ['Titanium Ingot', '3'] } }

    itemdict_en['Components']['Thruster'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Thruster', '1'] }, 
    'inputmaterial' :{ '1' : ['Steel', '2'], '2' : ['Copper Ingot', '3'] } }

    itemdict_en['Components']['Reinforced Thruster'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Reinforced Thruster', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Alloy', '5'], '2' : ['Electromagnetic Turbine', '5'] } }

    itemdict_en['Components']['Strange Matter'] = {'place' : 'Particle Collider', 
    'speed' : '7.5', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Strange Matter', '1'] }, 
    'inputmaterial' :{ '1' : ['Particle Container', '2'], '2' : ['Iron Ingot', '2'], '3' : ['Deuterium', '10'] } }

    #Category IV
    itemdict_en['Components']['Gear'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Gear', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '1'] } }

    itemdict_en['Components']['Electromagnetic Turbine'] = {'place' : 'Assembling Machine', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Electromagnetic Turbine', '1'] }, 
    'inputmaterial' :{ '1' : ['Electric Motor', '2'], '2' : ['Magnetic Coil', '2'] } }

    itemdict_en['Components']['Silicon Ore'] = {'place' : 'Smelter', 
    'speed' : '6', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Silicon Ore', '1'] }, 
    'inputmaterial' :{ '1' : ['Stone', '10'] } }

    itemdict_en['Components']['Circuit Board'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Circuit Board', '2'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '2'], '2' : ['Copper Ingot', '1'] } }

    itemdict_en['Components']['Graviton Lens'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Graviton Lens', '1'] }, 
    'inputmaterial' :{ '1' : ['Diamond', '4'], '2' : ['Strange Matter', '1'] } }

    itemdict_en['Components']['Sulfuric Acid'] = {'place' : 'Chemical Plant', 
    'speed' : '10', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Sulfuric Acid', '4'] }, 
    'inputmaterial' :{ '1' : ['Refined Oil', '6'], '2' : ['Stone', '8'], '3' : ['Water', '4'] } }

    itemdict_en['Components']['Deuterium'] = {'place' : 'Particle Collider', 
    'speed' : '12', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Deuterium', '5'] }, 
    'inputmaterial' :{ '1' : ['Hydrogen', '10'] } }

    itemdict_en['Components']['Plane Filter'] = {'place' : 'Assembling Machine', 
    'speed' : '5', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Plane Filter', '1'] }, 
    'inputmaterial' :{ '1' : ['Casimir Crystal', '1'], '2' : ['Titanium Glass', '2'] } }

    itemdict_en['Components']['Carbon Nanotube'] = {'place' : 'Chemical Plant', 
    'speed' : '15', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Carbon Nanotube', '2'] }, 
    'inputmaterial' :{ '1' : ['Graphene', '3'], '2' : ['Titanium Ingot', '1'] } }

    itemdict_en['Components']['Logistics Drone'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Logistics Drone', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '5'], '2' : ['Processor', '2'], '3' : ['Thruster', '2'] } }

    itemdict_en['Components']['Logistics Vessel'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Logistics Vessel', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Alloy', '10'], '2' : ['Processor', '10'], '3' : ['Reinforced Thruster', '2'] } }

    itemdict_en['Components']['Small Carrier Rocket'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Small Carrier Rocket', '1'] }, 
    'inputmaterial' :{ '1' : ['Dyson Sphere Components', '2'], '2' : ['Deuteron Fuel Rod', '2'], '3' : ['Quantum Chip', '2'] } }

    #Category V
    itemdict_en['Components']['Plasma Exciter'] = {'place' : 'Assembling Machine', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Plasma Exciter', '1'] }, 
    'inputmaterial' :{ '1' : ['Magnetic Coil', '4'], '2' : ['Prism', '2'] } }

    itemdict_en['Components']['Super-Magnetic Ring'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Super-Magnetic Ring', '1'] }, 
    'inputmaterial' :{ '1' : ['Electromagnetic Turbine', '2'], '2' : ['Magnet', '3'], '3' : ['Enegetic Graphite', '1'] } }

    itemdict_en['Components']['Particle Boardband'] = {'place' : 'Assembling Machine', 
    'speed' : '7.5', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Particle Boardband', '1'] }, 
    'inputmaterial' :{ '1' : ['Carbon Nanotube', '2'], '2' : ['Crystal Silicon', '2'], '3' : ['Plastic', '1'] } }

    itemdict_en['Components']['Processor'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Processor', '1'] }, 
    'inputmaterial' :{ '1' : ['Circuit Board', '2'], '2' : ['Microcrystalline Component', '2'] } }

    itemdict_en['Components']['Casimir Crystal'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Casimir Crystal', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Crystal', '1'], '2' : ['Graphene', '2'], '3' : ['Hydrogen', '12'] } }

    itemdict_en['Components']['Particle Container'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Particle Container', '1'] }, 
    'inputmaterial' :{ '1' : ['Electromagnetic Turbine', '2'], '2' : ['Copper Ingot', '2'], '3' : ['Graphene', '2'] } }

    itemdict_en['Components']['Space Warper'] = {'place' : 'Assembling Machine', 
    'speed' : '6', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Space Warper', '1'] }, 
    'inputmaterial' :{ '1' : ['Graviton Lens', '1'] } }

    itemdict_en['Components']['Annihilation Constraint Sphere'] = {'place' : 'Assembling Machine', 
    'speed' : '3', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Annihilation Constraint Sphere', '1'] }, 
    'inputmaterial' :{ '1' : ['Particle Container', '1'], '2' : ['Processor', '1'] } }

    itemdict_en['Components']['Recipe Carbon Nanotube Advanced'] = {'place' : 'Chemical Plant', 
    'speed' : '15', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Carbon Nanotube', '2'] }, 
    'inputmaterial' :{ '1' : ['Spiniform Stalagmite Crystal', '2'] } }

    itemdict_en['Components']['Solar Sail'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Solar Sail', '2'] }, 
    'inputmaterial' :{ '1' : ['Graphene', '1'], '2' : ['Photon Combiner', '1'] } }

    itemdict_en['Components']['Frame Material'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Frame Material', '1'] }, 
    'inputmaterial' :{ '1' : ['Carbon Nanotube', '4'], '2' : ['Titanium Alloy', '1'], '3' : ['High-Purity Silicon', '1'] } }

    itemdict_en['Components']['Dyson Sphere Component'] = {'place' : 'Assembling Machine', 
    'speed' : '7.5', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Dyson Sphere Component', '1'] }, 
    'inputmaterial' :{ '1' : ['Frame Material', '3'], '2' : ['Solar Sail', '3'], '3' : ['Processor', '3'] } }

    #Category VI
    itemdict_en['Components']['Photon Combiner'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Photon Combiner', '1'] }, 
    'inputmaterial' :{ '1' : ['Prism', '2'], '2' : ['Circuit Board', '1'] } }

    itemdict_en['Components']['Recipe Photon Combiner Advanced'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Photon Combiner', '1'] }, 
    'inputmaterial' :{ '1' : ['Optical Grating Crystal', '1'], '2' : ['Circuit Board', '1'] } }

    itemdict_en['Components']['Microcrystalline Component'] = {'place' : 'Assembling Machine', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Microcrystalline Component', '1'] }, 
    'inputmaterial' :{ '1' : ['High-Purity Silicon', '2'], '2' : ['Copper Ingot', '1'] } }

    itemdict_en['Components']['Quantum Chip'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Quantum Chip', '1'] }, 
    'inputmaterial' :{ '1' : ['Processor', '2'], '2' : ['Plane Filter', '2'] } }

    itemdict_en['Components']['Recipe Casimir Crystal Advanced'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Casimir Crystal', '1'] }, 
    'inputmaterial' :{ '1' : ['Optical Grating Crystal', '6'], '2' : ['Graphene', '2'], '3' : ['Hydrogen', '12'] } }

    itemdict_en['Components']['Recipe Particle Container Advanced'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Particle Container', '1'] }, 
    'inputmaterial' :{ '1' : ['Unipolar Magnet', '10'], '2' : ['Copper Ingot', '2'] } }

    itemdict_en['Components']['Recipe Space Warper Advanced'] = {'place' : 'Assembling Machine', 
    'speed' : '6', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Space Warper', '8'] }, 
    'inputmaterial' :{ '1' : ['Gravity Matrix', '1'] } }

    itemdict_en['Components']['Recipe Mass-Energy Storage'] = {'place' : 'Particle Collider', 
    'speed' : '30', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Antimatter', '2'], '2' : ['Hydrogen', '2'] }, 
    'inputmaterial' :{ '1' : ['Critical Photon', '2'] } }

    #Category VII
    itemdict_en['Components']['Electromagnetic Matrix'] = {'place' : 'Matrix Lab', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Electromagnetic Matrix', '1'] }, 
    'inputmaterial' :{ '1' : ['Magnetic Coil', '1'], '2' : ['Circuit Board', '1'] } }

    itemdict_en['Components']['Energy Matrix'] = {'place' : 'Matrix Lab', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Energy Matrix', '1'] }, 
    'inputmaterial' :{ '1' : ['Enegetic Graphite', '2'], '2' : ['Hydrogen', '2'] } }

    itemdict_en['Components']['Structure Matrix'] = {'place' : 'Matrix Lab', 
    'speed' : '7.5', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Structure Matrix', '1'] }, 
    'inputmaterial' :{ '1' : ['Diamond', '1'], '2' : ['Titanium Crystal', '1'] } }

    itemdict_en['Components']['Information Matrix'] = {'place' : 'Matrix Lab', 
    'speed' : '6', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Information Matrix', '1'] }, 
    'inputmaterial' :{ '1' : ['Processor', '2'], '2' : ['Particle Boardband', '1'] } }

    itemdict_en['Components']['Gravity Matrix'] = {'place' : 'Matrix Lab', 
    'speed' : '2.5', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Gravity Matrix', '1'] }, 
    'inputmaterial' :{ '1' : ['Graviton Lens', '1'], '2' : ['Quantum Chip', '1'] } }

    itemdict_en['Components']['Universe Matrix'] = {'place' : 'Matrix Lab', 
    'speed' : '4', 
    'Rep-ability' : 'False',
    'outcome' :{ '1' : ['Universe Matrix', '1'] }, 
    'inputmaterial' :{ '1' : ['Electromagnetic Matrix', '1'], '2' : ['Energy Matrix', '1'], '3' : ['Structure Matrix', '1'], '4' : ['Information Matrix', '1'], '5' : ['Gravity Matrix', '1'], '6' : ['Antimatter', '1'] } }

    itemdict_en['Components']['Foundation'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Foundation', '1'] }, 
    'inputmaterial' :{ '1' : ['Stone Brick', '3'], '2' : ['Steel', '1'] } }


    #Buildings

    #Category I
    itemdict_en['Buildings']['Tesla Tower'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Tesla Tower', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '2'], '2' : ['Magnetic Coil', '1'] } }

    itemdict_en['Buildings']['Wireless Power Tower'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Wireless Power Tower', '1'] }, 
    'inputmaterial' :{ '1' : ['Tesla Tower', '1'], '2' : ['Plasma Exciter', '3'] } }

    itemdict_en['Buildings']['Satellite Tower'] = {'place' : 'Assembling Machine', 
    'speed' : '12', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Satellite Tower', '1'] }, 
    'inputmaterial' :{ '1' : ['Wireless Power Tower', '1'], '2' : ['Super-Magnetic Ring', '10'], '3' : ['Frame Material', '2'] } }

    itemdict_en['Buildings']['Wind Turbine'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Wind Turbine', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '6'], '2' : ['Gear', '1'], '3' : ['Magnetic Coil', '3'] } }

    itemdict_en['Buildings']['Thermal Power Station'] = {'place' : 'Assembling Machine', 
    'speed' : '12', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Thermal Power Station', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '10'], '2' : ['Stone Brick', '4'], '3' : ['Gear', '4'], '4' : ['Magnetic Coil', '4'] } }

    itemdict_en['Buildings']['Solar Panel'] = {'place' : 'Assembling Machine', 
    'speed' : '12', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Solar Panel', '1'] }, 
    'inputmaterial' :{ '1' : ['Copper Ingot', '6'], '2' : ['High-Purity Silicon', '6'], '3' : ['Circuit Board', '4'] } }

    itemdict_en['Buildings']['Accumulator'] = {'place' : 'Assembling Machine', 
    'speed' : '12', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Accumulator', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '6'], '2' : ['Super-Magnetic Ring', '6'], '3' : ['Crystal Silicon', '4'] } }

    itemdict_en['Buildings']['Ray Receiver'] = {'place' : 'Assembling Machine', 
    'speed' : '7.5', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Ray Receiver', '1'] }, 
    'inputmaterial' :{ '1' : ['Steel', '20'], '2' : ['High-Purity Silicon', '20'], '3' : ['Photon Combiner', '10'], '4' : ['Processor', '5'], '5' : ['Super-Magnetic Ring', '20'] } }

    itemdict_en['Buildings']['Mini Fusion Power Station'] = {'place' : 'Assembling Machine', 
    'speed' : '6', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Mini Fusion Power Station', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Alloy', '12'], '2' : ['Super-Magnetic Ring', '10'], '3' : ['Carbon Nanotube', '8'], '4' : ['Processor', '4'] } }

    itemdict_en['Buildings']['Energy Exchanger'] = {'place' : 'Assembling Machine', 
    'speed' : '4', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Energy Exchanger', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Alloy', '40'], '2' : ['Steel', '40'], '3' : ['Processor', '40'], '4' : ['Particle Container', '8'] } }

    itemdict_en['Buildings']['Artificial Star'] = {'place' : 'Assembling Machine', 
    'speed' : '2', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Artificial Star', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Alloy', '20'], '2' : ['Frame Material', '20'], '3' : ['Annihilation Constraint Sphere', '10'], '4' : ['Quantum Chip', '10'] } }

    #Category II
    itemdict_en['Buildings']['Conveyor belt MK.I'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Conveyor belt MK.I', '3'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '2'], '2' : ['Gear', '1'] } }

    itemdict_en['Buildings']['Conveyor belt MK.II'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Conveyor belt MK.II', '3'] }, 
    'inputmaterial' :{ '1' : ['Conveyor belt MK.I', '3'], '2' : ['Electromagnetic Turbine', '1'] } }

    itemdict_en['Buildings']['Conveyor belt MK.III'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Conveyor belt MK.III', '3'] }, 
    'inputmaterial' :{ '1' : ['Conveyor belt MK.II', '3'], '2' : ['Super-Magnetic Ring', '1'], '3' : ['Graphene', '1'] } }

    itemdict_en['Buildings']['Splitter'] = {'place' : 'Assembling Machine', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Splitter', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '3'], '2' : ['Gear', '2'], '3' : ['Circuit Board', '1'] } }

    itemdict_en['Buildings']['Storage MK.I'] = {'place' : 'Assembling Machine', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Storage MK.I', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '4'], '2' : ['Stone Brick', '4'] } }

    itemdict_en['Buildings']['Storage MK.II'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Storage MK.II', '1'] }, 
    'inputmaterial' :{ '1' : ['Steel', '8'], '2' : ['Stone Brick', '8'] } }

    itemdict_en['Buildings']['Storage Tank'] = {'place' : 'Assembling Machine', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Storage Tank', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '8'], '2' : ['Stone Brick', '4'], '3' : ['Glass', '4'] } }

    itemdict_en['Buildings']['EM-Rail Ejector'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['EM-Rail Ejector', '1'] }, 
    'inputmaterial' :{ '1' : ['Steel', '20'], '2' : ['Gear', '20'], '3' : ['Processor', '5'], '4' : ['Super-Magnetic Ring', '10'] } }

    itemdict_en['Buildings']['Planetary Logistics Station'] = {'place' : 'Assembling Machine', 
    'speed' : '3', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Planetary Logistics Station', '1'] }, 
    'inputmaterial' :{ '1' : ['Steel', '40'], '2' : ['Titanium Ingot', '40'], '3' : ['Container', '40'], '4' : ['Particle Container', '20'] } }

    itemdict_en['Buildings']['Miniature Particle Collider'] = {'place' : 'Assembling Machine', 
    'speed' : '4', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Miniature Particle Collider', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Alloy', '20'], '2' : ['Frame Material', '20'], '3' : ['Super-Magnetic Ring', '50'], '4' : ['Graphene', '10'], '5' : ['Processor', '8'] } }

    #Category III
    itemdict_en['Buildings']['Sorter MK.I'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Sorter MK.I', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '1'], '2' : ['Circuit Board', '1'] } }

    itemdict_en['Buildings']['Sorter MK.II'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Sorter MK.II', '2'] }, 
    'inputmaterial' :{ '1' : ['Sorter MK.I', '2'], '2' : ['Electric Motor', '1'] } }

    itemdict_en['Buildings']['Sorter MK.III'] = {'place' : 'Assembling Machine', 
    'speed' : '60', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Sorter MK.III', '2'] }, 
    'inputmaterial' :{ '1' : ['Sorter MK.II', '2'], '2' : ['Electromagnetic Turbine', '1'] } }

    itemdict_en['Buildings']['Mining Machine'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Mining Machine', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '4'], '2' : ['Circuit Board', '2'], '3' : ['Magnetic Coil', '2'], '4' : ['Gear', '2'] } }

    itemdict_en['Buildings']['Water Pump'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Water Pump', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '8'], '2' : ['Stone Brick', '4'], '3' : ['Electric Motor', '4'], '4' : ['Circuit Board', '2'] } }

    itemdict_en['Buildings']['Oil Extractor'] = {'place' : 'Assembling Machine', 
    'speed' : '7.5', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Oil Extractor', '1'] }, 
    'inputmaterial' :{ '1' : ['Steel', '12'], '2' : ['Stone Brick', '12'], '3' : ['Circuit Board', '6'], '4' : ['Plasma Exciter', '4'] } }

    itemdict_en['Buildings']['Oil Refinery'] = {'place' : 'Assembling Machine', 
    'speed' : '10', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Oil Refinery', '1'] }, 
    'inputmaterial' :{ '1' : ['Steel', '10'], '2' : ['Stone Brick', '10'], '3' : ['Circuit Board', '6'], '4' : ['Plasma Exciter', '6'] } }

    itemdict_en['Buildings']['Vertical launching Silo'] = {'place' : 'Assembling Machine', 
    'speed' : '2', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Vertical launching Silo', '1'] }, 
    'inputmaterial' :{ '1' : ['Titanium Alloy', '80'], '2' : ['Frame material', '30'], '3' : ['Graviton Lens', '20'], '4' : ['Quantum Chip', '10'] } }

    itemdict_en['Buildings']['Interstella Logistics Station'] = {'place' : 'Assembling Machine', 
    'speed' : '2', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Interstella Logistics Station', '1'] }, 
    'inputmaterial' :{ '1' : ['Planetary Logistics Station', '1'], '2' : ['Titanium Alloy', '40'], '3' : ['Particle Container', '20'] } }

    #Category IV
    itemdict_en['Buildings']['Assembling Machine MK.I'] = {'place' : 'Assembling Machine', 
    'speed' : '30', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Assembling Machine MK.I', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '4'], '2' : ['Gear', '8'], '3' : ['Circuit Board', '4'] } }

    itemdict_en['Buildings']['Assembling Machine MK.II'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Assembling Machine MK.II', '1'] }, 
    'inputmaterial' :{ '1' : ['Assembling Machine MK.I', '1'], '2' : ['Graphene', '8'], '3' : ['Processor', '4'] } }

    itemdict_en['Buildings']['Assembling Machine MK.III'] = {'place' : 'Assembling Machine', 
    'speed' : '15', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Assembling Machine MK.III', '1'] }, 
    'inputmaterial' :{ '1' : ['Assembling Machine MK.II', '1'], '2' : ['Particle Boardband', '8'], '3' : ['Quantum Chip', '2'] } }

    itemdict_en['Buildings']['Smelter'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Smelter', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '4'], '2' : ['Stone Brick', '2'], '3' : ['Circuit Board', '4'], '4' : ['Magnetic Coil', '2'] } }

    itemdict_en['Buildings']['Fractionator'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Fractionator', '1'] }, 
    'inputmaterial' :{ '1' : ['Steel', '8'], '2' : ['Stone Brick', '4'], '3' : ['Glass', '4'], '4' : ['Processor', '1'] } }

    itemdict_en['Buildings']['Chemical Plant'] = {'place' : 'Assembling Machine', 
    'speed' : '12', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Chemical Plant', '1'] }, 
    'inputmaterial' :{ '1' : ['Steel', '8'], '2' : ['Stone Brick', '8'], '3' : ['Glass', '8'], '4' : ['Circuit Board', '2'] } }

    itemdict_en['Buildings']['Matrix Lab'] = {'place' : 'Assembling Machine', 
    'speed' : '20', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Matrix Lab', '1'] }, 
    'inputmaterial' :{ '1' : ['Iron Ingot', '8'], '2' : ['Glass', '4'], '3' : ['Circuit Board', '4'], '3' : ['Magnetic Coil', '4'] } }

    itemdict_en['Buildings']['Orbital Collector'] = {'place' : 'Assembling Machine', 
    'speed' : '2', 
    'Rep-ability' : 'True',
    'outcome' :{ '1' : ['Orbital Collector', '1'] }, 
    'inputmaterial' :{ '1' : ['Interstella Logistics Station', '1'], '2' : ['Super-Magnetic Ring', '50'], '3' : ['Reinforced Thruster', '20'], '4' : ['Accumulator(Full)', '20'] } }


    # itemdict_en['Buildings']['Orbital Collector'] = {'place' : 'Assembling Machine', 
    # 'speed' : 'amountperminute', 
    # 'Rep-ability' : 'True',
    # 'outcome' :{ '1' : ['Orbital Collector', '1'] }, 
    # 'inputmaterial' :{ '1' : ['name1', 'amount1'], '2' : ['name2', 'amount2'], '3' : ['name3', 'amount3'] } }
    return itemdict_en


path = Path(os.getcwd())
# filepath_cn = path/'itemdata_cn.txt'
filepath_en = path/'itemdata_en.txt'
filepath_translator = path/'translator.txt'


# if os.path.exists(filepath_cn):
#     f = open(filepath_cn, 'w')
# else:
#     f = open(filepath_cn, 'x')
Componentsdict = getitems()
if os.path.exists(filepath_en):
    f = open(filepath_en, 'w')
    json.dump(Componentsdict,f)
else:
    f = open(filepath_en, 'x')
    json.dump(Componentsdict,f)




f.close()