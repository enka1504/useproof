# Useproof Site

This directory contains the product website served at `http://88.99.149.112:3333/`.

## Pages

- `index.html`: product homepage
- `product.html`: product overview
- `examples.html`: casefile examples
- `docs.html`: quickstart and source docs
- `pricing.html`: open-source and hosted product path

## Run Locally

```bash
cd /root/useproof
python3 -m http.server 3333 --bind 0.0.0.0 --directory site
```

The current public service is managed with:

```bash
systemctl status useproof-3333 --no-pager
systemctl restart useproof-3333
systemctl stop useproof-3333
```

For persistent hosting, install the unit in `deploy/useproof-site.service`.
