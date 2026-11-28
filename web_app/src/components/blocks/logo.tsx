import { IconHexagons } from '@tabler/icons-react';
import { cn } from 'cn';

type LogoProps = {
  className?: string;
  showWordmark?: boolean;
};

export function Logo({ className, showWordmark = true }: LogoProps) {
  return (
    <span className={cn('inline-flex items-center gap-2', className)}>
      <span className='flex size-8 items-center justify-center rounded-lg bg-primary text-primary-foreground'>
        <IconHexagons className='size-5' />
      </span>
      {showWordmark && <span className='font-heading text-base font-semibold text-foreground'>HDBeePrice</span>}
    </span>
  );
}
