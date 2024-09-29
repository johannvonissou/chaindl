# OCFINANCE

Download On-Chain data from a variety of sources

## Installation
Use pip to install the ocfinance package.
```bash
pip install ocfinance
```

## Supported Websites
- **[CheckOnChain](https://charts.checkonchain.com/)** (recommended)
- **[ChainExposed](https://chainexposed.com/)** (recommended)
- [Bitbo Charts](https://charts.bitbo.io/) (very slow)

## Usage
Get the url of the chart and download it:

```python
import ocfinance as of
data = of.download("https://charts.checkonchain.com/btconchain/pricing/pricing_picycleindicator/pricing_picycleindicator_light.html")
```
