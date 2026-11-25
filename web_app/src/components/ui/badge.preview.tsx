import { IconCheck, IconClock, IconX } from '@tabler/icons-react';

import { Badge } from '@/components/ui/badge';

export const Variants = () => (
  <div className='flex flex-wrap items-center gap-2'>
    <Badge>Default</Badge>
    <Badge variant='secondary'>Secondary</Badge>
    <Badge variant='destructive'>Destructive</Badge>
    <Badge variant='outline'>Outline</Badge>
    <Badge variant='ghost'>Ghost</Badge>
    <Badge variant='link'>Link</Badge>
  </div>
);

export const WithIcons = () => (
  <div className='flex flex-wrap items-center gap-2'>
    <Badge>
      <IconCheck />
      Completed
    </Badge>
    <Badge variant='secondary'>
      <IconClock />
      Pending
    </Badge>
    <Badge variant='destructive'>
      <IconX />
      Failed
    </Badge>
  </div>
);

export const AsLink = () => (
  <div className='flex flex-wrap items-center gap-2'>
    <Badge variant='outline' render={<a href='#badge-outline-link' />}>
      Outline link
    </Badge>
    <Badge variant='link' render={<a href='#badge-link' />}>
      Text link
    </Badge>
  </div>
);
