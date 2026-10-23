import { defineConfig } from "orval";

export default defineConfig({
  services: {
    input: "../api_services/openapi/spec.json",
    output: {
      mode: "tags",
      target: "./src/api/",
      client: "react-query",
      httpClient: "axios",
    },
  },
  sevicesZod: {
    input: "../api_services/openapi/spec.json",
    output: {
      mode: "tags",
      client: "zod",
      target: "./src/api/",
      fileExtension: ".zod.ts",
      override: {
        zod: {
          variant: "mini",
          version: 4,
        },
      },
    },
  },
});
