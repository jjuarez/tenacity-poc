# Tenacity POC

A Qick test of the [tenacity](https://tenacity.readthedocs.io/en/latest/) library and also this projects
pretends to be somekind of [Grafana k6](https://k6.io/) tool testing.

## Getting started
1. Set up the project, to do so we need to set up two different stacks, the Node.js and the python one executing this simple command:
  ```bash
  make setup
  ```
  remember, it's very convenient to activate the environment to avoid possible errors (`source .venv/bin/activate`)

2. Start the HTTP server
  ```bash
  make server
  ```
3. Testing the tenacity retries:
  ```bash
  make client
  ```

### Testing the HTTP server using k6s
After has started the HTTP server you should launch the k6 script, easy peacy:
```bash
make test/performance
```
