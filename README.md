# OCFINANCE (Works with Cryptoquant)

Download On-Chain data from cryptoquant, checkonchain, etc.

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
- [Bitbo Charts](https://charts.bitbo.io/) (slow)
- [Bitcoin Magazine Pro](https://www.bitcoinmagazinepro.com) (slow)

## Usage
Get the url of the chart and download it:

```python
import ocfinance as of
data = of.download("https://charts.checkonchain.com/btconchain/pricing/pricing_picycleindicator/pricing_picycleindicator_light.html")

# Export as CSV
data.to_csv('out.csv')
```
## Cryptoquant guide
**_Email and password of your account are required._**

**Works only with third party indicators**

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
The url that needs to be passed can be accessed by clicking the source button and copying that url (follow the images):

![Click the source button](/assets/cryptoquant_step1.png)
![Copy the url](/assets/cryptoquant_step2.png)

## Running tests
#### Optional
To run integration test for cryptoquant, add your cryptoquant account's email and password to .env.sample. Rename the file into .env. These tests will be otherwise be skipped

#### Run
```bash
git clone https://github.com/dhruvan2006/ocfinance
pip install pytest dotenv
pytest
```
