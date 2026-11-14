# ComposeKit

A project to simplify Docker container management, made with love.

It ships a single `composekit` command with three subcommands:
- `composekit sort`: sorts keys in Docker Compose files
- `composekit update`: updates Docker images
- `composekit generate`: creates Docker Compose files

See the [examples/](examples/) directory for sample container definitions
and config files you can copy and adapt:
- Generation rules: [examples/generate.yaml](examples/generate.yaml)
- Update rules: [examples/update.yaml](examples/update.yaml)
- Container definitions: [examples/containers/](examples/containers/)

## Installation

Install directly from the repository with [uv](https://docs.astral.sh/uv):
```bash
uv tool install git+https://github.com/6AMStuff/ComposeKit
```
or with [pipx](https://pipx.pypa.io/):
```bash
pipx install git+https://github.com/6AMStuff/ComposeKit
```

Pin a release by appending `@<tag>`, e.g. `@v1.0.0`.

## Usage

Each subcommand reads container definitions from a folder (defaulting to
`containers/` in the current directory) and writes the generated compose
files relative to where you run it. Point it at your own files with flags:
```bash
composekit generate -c config/generate.yaml
composekit update -c config/update.yaml
composekit sort -C containers/
```

To try it against the bundled examples from the repo root:
```bash
composekit generate -c examples/generate.yaml
```

Common flags:
- `-C/--containers PATH`: folder with container definitions
- `-c/--config PATH`: config file to load (repeatable)
- `--commit`: commit the resulting changes to the git repository (off by
  default; intended for CI)

Generate also accepts `-o/--composes PATH` and `--output PATH`. See
`composekit <command> --help` for the full list.

## Configuration

Config files are YAML. Without `-c`, each command loads its default paths:

| Command | Default config |
| --- | --- |
| `generate`, `sort` | `config/generate.yaml` |
| `update` | `config/update.yaml`, then `config/update.private.yaml` (later wins) |

Any top-level option can also be set with an uppercase environment
variable, which takes precedence over the file (e.g. `LIMIT=100`).

### Generate and sort options

| Option | Default | Description |
| --- | --- | --- |
| `containers_folder` | `containers` | Folder with container definitions. |
| `composes_folder` | `composes` | Folder to write per-service compose files into. |
| `network_name` | `cloud` | Name of the shared Docker network. |
| `network_driver` | `bridge` | Driver of the shared network. |
| `subnet` | `172.20.0.0/24` | Subnet of the shared network. |
| `restart_policy` | `unless-stopped` | Default restart policy for services. |
| `use_full_directory` | `true` | When exactly one relative volume exists, bind it to `bind_path/<folder>` instead of a subfolder. |
| `capitalize_folder_name` | `non_custom` | Capitalize folder names: `full` always, `non_custom` only when `folder` is not set, any other value never. |
| `bind_path` | `/home/docker/Docker` | Host directory containing per-service data. |
| `output` | `docker-compose.yaml` | Path of the aggregated main compose file. |

`sort` only uses `containers_folder`; the rest apply to `generate`.

### Update options

| Option | Default | Description |
| --- | --- | --- |
| `containers_folder` | `containers` | Folder with container definitions. |
| `default_registry` | `docker.io` | Registry used for images that do not specify one. |
| `limit` | `40` | Number of newest matching tags to consider. |
| `timeout` | `10` | Registry request timeout, in seconds. |

Per-image options can be set under the full image name (`registry/user/image`),
`user/image`, or just `image`. They are checked in that order and the first
match wins:

```yaml
limit: 40

cloudflare/cloudflared:
  date_versions: true

linuxserver/nginx:
  update: false

ghcr.io/private/image:
  version_regex: '^v(\d+)\.(\d+)\.(\d+)$'
  username: my-user
  password: my-token
```

| Option | Description |
| --- | --- |
| `update` | Set to `false` to skip updates for this image. |
| `date_versions` | Set to `true` to use date versions (`v?YYYY.M.D`) instead of semantic versions. |
| `version_regex` | Custom regex with capture groups; the groups are joined with dots to form the version. Takes precedence over `date_versions`. |
| `limit` | Per-image override of the number of tags to consider. |
| `username`, `password` | Registry credentials for private images; both must be set. |

By default `update` matches semantic versions (`v?MAJOR.MINOR[.PATCH]`),
ignores pre-releases and non-matching tags, and only writes versions newer
than the current tag.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.
