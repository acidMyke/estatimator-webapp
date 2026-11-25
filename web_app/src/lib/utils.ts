import type { ComponentType } from 'react';

export { cn } from 'cn';

export function isComponentType(value: unknown): value is ComponentType<any> {
  if (typeof value === 'function') {
    return true;
  }

  if (typeof value === 'object' && value !== null && '$$typeof' in value) {
    return true;
  }

  return false;
}