import { createFileRoute, Link, redirect } from '@tanstack/react-router';
import { type ComponentType } from 'react';

import { Separator } from '@/components/ui/separator';

type PreviewModule = Record<string, ComponentType>;

const previewFiles = import.meta.glob<PreviewModule>('@/components/blocks/*.preview.tsx', {
  eager: true,
});

const filepaths = Object.keys(previewFiles);
const filenameMapping = Object.fromEntries(
  filepaths.map(path => [path.replace('/src/components/blocks/', '').replace('.preview.tsx', ''), path]),
);

const fileKeys = Object.keys(filenameMapping).sort((a, b) => a.localeCompare(b));

export const Route = createFileRoute('/preview/components/blocks/{-$file}/{-$cname}')({
  component: RouteComponent,
  beforeLoad: ({ params }) => {
    if (!params.file) return;
    if (!(params.file in filenameMapping)) {
      throw redirect({ to: '.', params: { file: undefined, cname: undefined } });
    }
    if (params.cname) {
      const mod = previewFiles[filenameMapping[params.file]];
      if (!(params.cname in mod)) {
        throw redirect({ to: '.', params: { file: undefined, cname: undefined } });
      }
    }
  },
});

function RouteComponent() {
  const { file, cname } = Route.useParams();

  const activeFile = file ?? fileKeys[0];
  const Component = activeFile && cname ? previewFiles[filenameMapping[activeFile]][cname] : undefined;

  return (
    <div className='flex h-screen bg-neutral-50 text-neutral-900'>
      <div className='w-64 shrink-0 overflow-y-auto border-r bg-white p-3'>
        <div className='mb-3 px-2 text-xs font-bold tracking-wider text-neutral-500 uppercase'>
          Blocks ({fileKeys.length})
        </div>

        <div className='space-y-1'>
          {fileKeys.map(fileKey => {
            const isCurrentFile = fileKey === activeFile;
            const mod = previewFiles[filenameMapping[fileKey]];
            const exportsInFile = Object.keys(mod);

            return (
              <div key={fileKey}>
                <div className='flex items-center justify-between rounded-md text-xs'>
                  <Link
                    to='/preview/components/blocks/{-$file}/{-$cname}'
                    params={{ file: fileKey }}
                    className='flex-1 truncate px-2.5 py-1.5 font-semibold'
                  >
                    {fileKey}
                  </Link>
                </div>

                {exportsInFile.length > 0 && (
                  <ul className='mt-1 ml-2.5 space-y-0.5 border-l border-neutral-200 pl-2'>
                    {exportsInFile.map(expName => {
                      const isCurrentComp = isCurrentFile && cname === expName;
                      return (
                        <li key={expName}>
                          <Link
                            to='/preview/components/blocks/{-$file}/{-$cname}'
                            params={{ file: fileKey, cname: expName }}
                            className='block truncate rounded-md px-2.5 py-1 text-xs text-neutral-600 hover:bg-neutral-100 hover:text-neutral-900 data-[active="true"]:bg-neutral-900 data-[active="true"]:font-medium data-[active="true"]:text-white'
                            data-active={isCurrentComp}
                          >
                            {expName}
                          </Link>
                        </li>
                      );
                    })}
                  </ul>
                )}
              </div>
            );
          })}
        </div>
      </div>

      <div className='flex-1 overflow-y-auto p-8'>
        {!Component ? (
          <p className='text-sm text-neutral-500'>No block *.preview.tsx files found.</p>
        ) : (
          <div className='mx-auto max-w-5xl space-y-8'>
            <h2 className='text-xl font-bold'>
              {activeFile} / {cname}
            </h2>
            <Separator />

            <div className='bg-white p-6 shadow-xs'>
              <Component />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
