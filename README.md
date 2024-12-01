# Investment Planner Using Linear Programming
Involving 3 Variables :  
- X = Saham
- Y = Obligasi
- Z = Real Estate (Property)

Seluruh investasi harus sesuai budget,  
> x + y + z <= Total Pool

Maksimum investasi di saham,  
> x + 0y + 0z <= Pool * 50%

Minimum investasi di obligasi,
> 0x + 1y + 0z >= Pool * 15%

Minimum investasi di properti,  
> 0x + 0y + z >= Pool * 25% 

### Developing
``` pip install -r requirements.txt ```
