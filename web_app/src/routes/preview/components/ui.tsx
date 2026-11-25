import { createFileRoute } from '@tanstack/react-router';
import { type ComponentType } from 'react';

import { isComponentType } from '@/lib/utils';

const previewSections = Object.entries(import.meta.glob('@/components/ui/*.preview.tsx', { eager: true })).map(
  ([path, module]) => {
    if (typeof module !== 'object' || module == null) return { filename: '', sections: [] };
    const filename = path.replace('/src/components/ui/', '');
    const sections: { name: string; Component: ComponentType }[] = [];
    for (const key in module) {
      const item = (module as Record<string, unknown>)[key];
      if (isComponentType(item)) {
        sections.push({ name: key, Component: item });
      }
    }
    return { filename, sections };
  },
);

export const Route = createFileRoute('/preview/components/ui')({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className='flex-1 overflow-y-auto p-8 space-y-8'>
      {previewSections.map(({ filename, sections }) => (
        <div className='mx-auto max-w-5xl space-y-8'>
          <div className='border-b pb-4'>
            <h2 className='text-xl font-bold'>{filename}</h2>
          </div>
          {sections.map(({ name, Component }) => (
            <div key={name} className='rounded-lg border bg-white p-6 shadow-xs'>
              <h3 className='mb-4 text-xs font-semibold uppercase tracking-wider text-neutral-400'>{name}</h3>
              <Component />
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}
