import { createFileRoute } from '@tanstack/react-router';
import { type ComponentType } from 'react';

import { isComponentType } from '@/lib/utils';

type PreviewSection = { name: string; Component: ComponentType };

const previewSections = Object.entries(import.meta.glob('@/components/ui/*.preview.tsx', { eager: true }))
  .map(([path, module]) => {
    if (typeof module !== 'object' || module == null) return { filename: '', anchor: '', sections: [] };
    const filename = path.replace('/src/components/ui/', '');
    const anchor = filename
      .replace(/\.preview\.tsx$/, '')
      .replace(/[^a-zA-Z0-9]+/g, '-')
      .toLowerCase();
    const sections: PreviewSection[] = [];
    for (const key in module) {
      const item = (module as Record<string, unknown>)[key];
      if (isComponentType(item)) {
        sections.push({ name: key, Component: item });
      }
    }
    return { filename, anchor, sections };
  })
  .filter(preview => preview.filename !== '');

export const Route = createFileRoute('/preview/components/ui')({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className='flex flex-1 flex-col gap-8 overflow-y-auto p-8'>
      <nav
        id='ui-preview-top'
        aria-label='Component previews'
        className='mx-auto w-full max-w-5xl scroll-mt-8 rounded-lg border bg-muted/40 p-4'
      >
        <h1 className='mb-3 text-sm font-semibold'>Component previews</h1>
        <ul className='grid grid-cols-2 gap-x-6 gap-y-1 sm:grid-cols-3 lg:grid-cols-4'>
          {previewSections.map(({ anchor }) => (
            <li key={anchor}>
              <a
                href={`#${anchor}`}
                className='text-sm text-muted-foreground underline-offset-4 hover:text-foreground hover:underline'
              >
                {anchor}
              </a>
            </li>
          ))}
        </ul>
      </nav>
      {previewSections.map(({ filename, anchor, sections }) => (
        <section key={anchor} id={anchor} className='mx-auto flex w-full max-w-5xl scroll-mt-8 flex-col gap-8'>
          <div className='border-b pb-4'>
            <h2 className='text-xl font-bold'>{filename}</h2>
          </div>
          {sections.map(({ name, Component }) => (
            <div key={name} className='rounded-lg border bg-white p-6 shadow-xs'>
              <h3 className='mb-4 text-xs font-semibold uppercase tracking-wider text-neutral-400'>{name}</h3>
              <Component />
            </div>
          ))}
          <div className='flex justify-end border-t pt-4'>
            <a
              href='#ui-preview-top'
              className='text-sm text-muted-foreground underline-offset-4 hover:text-foreground hover:underline'
            >
              Back to top
            </a>
          </div>
        </section>
      ))}
    </div>
  );
}
