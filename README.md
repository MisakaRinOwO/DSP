# DSP
Dyson Sphere Project utility tool working in progress.


Speeds for items produced by assembling machines are assumed to be 1.0x (Equals to replicator speed after '''Quantum Printing Technology''' has been researched.)

databse file format:

{'Components/Buildings' : 
    {'item name' : 
        {'place' : 'Facility', 
            'speed' : 'amountperminute', 
            'Rep-ability' : 'True'/'False',
            'outcome' : { '1' : ['name', 'amount1'] , etc...  }, 
            'input material' : { '1' : ['name1', 'amount1'], etc...  } 
        }
    }
}
