import { Button } from '@/components/ui/button';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip';

export const Demo = () => (
  <TooltipProvider>
    <Tooltip>
      <TooltipTrigger render={<Button variant='outline' />}>Hover me</TooltipTrigger>
      <TooltipContent>Add to library</TooltipContent>
    </Tooltip>
  </TooltipProvider>
);

export const Sides = () => (
  <TooltipProvider>
    <div className='flex flex-wrap items-center gap-2'>
      {(['top', 'right', 'bottom', 'left'] as const).map(side => (
        <Tooltip key={side}>
          <TooltipTrigger render={<Button variant='outline' className='capitalize' />}>{side}</TooltipTrigger>
          <TooltipContent side={side}>Tooltip on the {side}</TooltipContent>
        </Tooltip>
      ))}
    </div>
  </TooltipProvider>
);

export const WithShortcut = () => (
  <TooltipProvider delay={200}>
    <Tooltip>
      <TooltipTrigger render={<Button variant='ghost' />}>Search</TooltipTrigger>
      <TooltipContent>
        Open search
        <kbd data-slot='kbd' className='rounded-sm bg-background/20 px-1.5 font-mono text-[10px]'>
          ⌘K
        </kbd>
      </TooltipContent>
    </Tooltip>
  </TooltipProvider>
);
