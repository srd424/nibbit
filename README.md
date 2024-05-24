# Usage

`start-prefetch` will attempt to fetch a runtime closure for an attribute path via bittorrent using aria2. At the moment
the closure is computed by following `References:` headers in the `.narinfo`s, so the whole closure must be available. Later on
we might be able to work around incomplete runtime closures by using the build-time closure instead.

0. `./dev` to get a nix-shell with deps
1. Start aria2c: `aria2c -D --enable-rpc=true --bt-detach-seed-only=true`
2. Checkout a repo of torrent & narinfos, e.g. https://github.com/srd424/aux-torrent, set `REPO_DIR` to checkout dir
3. Set `NIX_EXPR` to a path containing a nix expression, e.g. a checkout of https://github.com/auxolotl/core
4. Set `ATTR_PATH` to a nix attribute path, e.g. `stdenv`
5. run `start-prefetch`

`aria2p show` can be used to monitor download progress; downloads will go to `DL_DIR`, by default `~/.cache/nibbit/nix`. When finished,
`nix --extra-experimental-features nix-command copy --from file://$HOME/.cache/nibbit/nix <STORE_PATH>`should import the cached binaries
into your nix store (the top-level `<STORE_PATH>` is printed by `start-prefetch`.)

# TODOs

- a proper command line
- a config file
- tool to check if the download of a given closure has finished (which could then automatically import the nars)
- a proper tool to 'publish' torrents
- a cleanup/prune tool to remove older torrents (maybe anything that's not in the subscribed/published closures, possibly plus a few older files up to a defined limit)
- support for multiple simultaneous expression + attribute combinations
