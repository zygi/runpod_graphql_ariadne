# Usage
A third-party RunPod GraphQL client in Python generated using Ariadne.
The author is not affiliated with RunPod. This package will be updated to match the API on a best effort basis.

# Development
To regenerate the package:
1) Install dev dependencies: `pip install -r pyproject.toml --extra dev` 
1) Fetch https://graphql-spec.runpod.io/ and convert it to markdown to reduce the size
2) Ask your favorite AI to convert it into a valid GraphQL schema `runpod.schema`
4) Run `ariadne-codegen`