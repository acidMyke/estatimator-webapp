import { defineConfig, pascal } from 'orval';

export default defineConfig({
  services: {
    input: {
      target: '../api_services/openapi/spec.json',
      filters: {
        mode: 'exclude',
        tags: ['System'],
      },
    },
    output: {
      mode: 'tags',
      client: 'react-query',
      target: './src/api/',
      formatter: 'oxfmt',
      httpClient: 'axios',
      schemas: { type: 'zod', path: './src/api/', mode: 'single' },
      override: {
        query: {
          useSkipToken: true,
        },
        zod: {
          variant: 'mini',
          version: 4,
        },
        operationName(operation, route, verb) {
          const pathSegments = route
            .replace(/[{}]/g, '')
            .split(/[/_.-]/)
            .filter(Boolean);

          const formattedPath = pascal(pathSegments.join('-'));
          const firstTag = pascal(operation.tags?.[0] ?? '');
          const operationId = pascal(operation.summary ?? '');

          if (formattedPath.includes(firstTag)) {
            return `${verb}${formattedPath}${operationId}`;
          }
          return `${verb}${firstTag}${formattedPath}${operationId}`;
        },
      },
    },
  },
});
