# OCFINANCE

Download On-Chain data from a variety of sources

## Installation
Use pip to install the ocfinance package.
```bash
pip install ocfinance
```

## Supported Websites
- [CheckOnChain](https://charts.checkonchain.com/)
- [ChainExposed](https://chainexposed.com/)

## Usage
Get the url of the chart and download it:

```python
import ocfinance as of
data = of.download("https://charts.checkonchain.com/btconchain/pricing/pricing_picycleindicator/pricing_picycleindicator_light.html")

# Access a specific column with
btc = data['Price']
```
