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
- **[Woocharts](https://woocharts.com/)** (recommended)
- **[Cryptoquant](https://cryptoquant.com/)** (_follow guide below_)
- [Bitbo Charts](https://charts.bitbo.io/) (very slow)

## Usage
Get the url of the chart and download it:

```python
import ocfinance as of
data = of.download("https://charts.checkonchain.com/btconchain/pricing/pricing_picycleindicator/pricing_picycleindicator_light.html")
```
## Cryptoquant guide
_Email and password of your account are required._

Pass your email and password to the download function (preferably using environment variables)
```python
import os
import ocfinance as of

email = os.getenv('CRYPTOQUANT_EMAIL')
password = os.getenv('CRYPTOQUANT_PASSWORD')

data = of.download(
    "https://cryptoquant.com/analytics/query/66451fd6f3cac64b85386229?v=66451fd6f3cac64b8538622b",
    email=email,
    password=password
)
```
The  url that needs to be passed can be access like so:

![Click the source button](/assets/cryptoquant_step1.png)
![Copy the url](/assets/cryptoquant_step2.png)
