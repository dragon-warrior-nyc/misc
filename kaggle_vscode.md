# Kaggle + VS Code — Quick Guide

This document explains how I connect VS Code to Kaggle: authentication, syncing files (pull/push), and how I run code on Kaggle's remote notebook environment and retrieve outputs.

## Prerequisites
- Install the Kaggle CLI: `pip install kaggle` (or use `pipx`/venv).
- Create a Kaggle API token: Account → API → "API Tokens (Recommended)"
- Set the `KAGGLE_API_TOKEN` environment variable
```bash
export KAGGLE_API_TOKEN=<YOUR API TOKEN>
```

## Local workflow in VS Code (edit & test locally)
- Open the project folder in VS Code and edit notebooks (`.ipynb`) or scripts (`.py`).
- Recommended VS Code extensions: **Python**, **Jupyter**.
- For notebooks: use the Jupyter extension's Interactive Window to run cells locally before pushing.

## Syncing kernels (notebooks) with Kaggle
Kaggle notebooks (kernels) are synced using the Kaggle CLI `kernels` commands.

- Pull an existing kernel to a local folder:

```bash
kaggle kernels pull <owner>/<kernel-slug> -p path/to/local/folder
```

- Edit in VS Code.

- Push changes back to Kaggle:

```bash
# from the folder that contains kernel-metadata.json and the notebook
kaggle kernels push -p path/to/local/folder
```

Notes:
- The local folder should be the kernel directory (contains `kernel-metadata.json` and the notebook file).
- `kaggle kernels push` updates the notebook on Kaggle. Use descriptive commit-style messages inside `kernel-metadata.json` if needed.

## Syncing datasets
- To create / update a dataset from a local folder:

```bash
kaggle datasets create -p path/to/dataset --dir-mode zip  # first time
kaggle datasets version -p path/to/dataset -m "Update: notes"  # to push a new version
```

## Connecting to a Live Kaggle Jupyter Server (polished)

Short note: Kaggle's web UI may expose a "VS Code compatible" connection URL in the Run sidebar for some notebook sessions. When present, that URL lets you connect VS Code's Jupyter client to the notebook's remote kernel so you can run cells from your editor. If you don't see a connection URL in the Kaggle Run sidebar, use the alternatives described earlier (cloud VM, Remote-SSH, or push/run on the Kaggle site).

Steps (when a VS Code-compatible URL is available):

- 1) Start a Kaggle session

  - Open the notebook on the Kaggle website and start the session (Run → Start or Start Session).

- 2) Get the connection URL

  - In the Kaggle notebook page open the Run (right) sidebar. If Kaggle provides a connection, it will show a "VS Code compatible URL" or "Jupyter server URL" entry. Click copy to copy the full URL (it typically contains a token parameter).

- 3) Connect from VS Code

  - Install and enable the **Jupyter** extension in VS Code.
  - Open any `.ipynb` file or create a new notebook.
  - Click the kernel selector (top-right) → choose **Existing Jupyter Server...** (or open the Command Palette and run `Jupyter: Specify Jupyter server for connections`).
  - Paste the copied URL (example format: `https://<host>/?token=...`) and press Enter.

- 4) Confirm and use

  - VS Code will connect to the remote kernel and list available kernels. Select the kernel you want and run cells as usual; execution happens on Kaggle's runtime (including any assigned GPU/TPU).

Security & reliability notes

- Treat the copied URL as a secret: the URL includes an access token that can control the notebook session. Do not share it.
- Sessions can expire or be preempted; the connection may drop — save work and use `kaggle kernels push` to persist changes.
- Connecting this way does not automatically sync notebook files back to Kaggle's kernel source. After editing locally, follow the push/pull steps to update the kernel on Kaggle.
- If you do not see a VS Code-compatible URL in the Run sidebar, Kaggle may not expose that feature for the notebook or your account; use the alternatives above.

If you'd like, I can add a short screenshot-style step list or a small checklist you can paste into the notebook README explaining how to copy the URL and connect from VS Code.


## Retrieving outputs and artifacts
- After running a kernel on Kaggle, download produced files (if the kernel was set to save output) via:

```bash
kaggle kernels output <owner>/<kernel-slug> -p path/to/download
```

This fetches files saved as kernel outputs into the specified local path.

## Helpful VS Code tips
- Use the Jupyter extension to open the `.ipynb` files directly in VS Code.
- When editing notebooks locally, keep the kernel folder structure (include `kernel-metadata.json`) so `kaggle kernels push` works.
- Use a local git repo for version control; treat Kaggle as a deployment target (push/pull there as needed).

## Example quick-sync script
Create `sync-kaggle.sh` in your kernel folder to simplify push/pull:

```bash
#!/usr/bin/env bash
set -e
case "$1" in
  pull)
    kaggle kernels pull "$2" -p .
    ;;
  push)
    kaggle kernels push -p .
    ;;
  output)
    kaggle kernels output "$2" -p ./output
    ;;
  *)
    echo "Usage: $0 {pull <owner/slug>|push|output <owner/slug>}"
    exit 1
    ;;
esac
```

Make it executable: `chmod +x sync-kaggle.sh`.

## Examples — Running `sync-kaggle.sh` in the terminal
Here are concrete examples you can copy-paste from your kernel folder.

- Pull a kernel into the current folder (replace owner/slug):

```bash
./sync-kaggle.sh pull your-username/your-kernel-slug
```

- Push local changes from the current folder to Kaggle:

```bash
./sync-kaggle.sh push
```

- Download kernel outputs into an `output/` folder:

```bash
./sync-kaggle.sh output your-username/your-kernel-slug
# then view files in ./output
ls -la ./output
```

- Run the script from anywhere by giving the full path to the kernel folder:

```bash
/path/to/your/kernel/folder/sync-kaggle.sh push
```

- Quick one-liner to pull then open the notebook in VS Code (macOS example):

```bash
./sync-kaggle.sh pull your-username/your-kernel-slug && code .
```

Notes:
- If you get "permission denied", re-run `chmod +x sync-kaggle.sh` or run `bash sync-kaggle.sh ...`.
- Replace `your-username/your-kernel-slug` with the actual kernel identifier (owner/slug) from the Kaggle URL.


## Troubleshooting & notes
- If `kaggle` CLI reports authentication errors, confirm `~/.kaggle/kaggle.json` exists and has `chmod 600`.
- If push fails, check `kernel-metadata.json` for valid fields and that file names match the metadata.
- For large data, use `kaggle datasets` instead of embedding large files in kernels.

## Next steps / suggestions
- If you need direct VS Code remote editing on a hosted Jupyter server, I can add steps for creating a small cloud VM + remote Jupyter server and how to connect VS Code to it.

---

Last updated: 2025-12-31
