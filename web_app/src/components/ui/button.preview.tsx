// src/components/ui/Button.preview.tsx
import { useState } from 'react';

import { Button } from '@/components/ui/button';

export const Variants = () => (
  <div className='flex flex-wrap items-center gap-3'>
    <Button variant='default'>Primary</Button>
    <Button variant='outline'>Outline</Button>
    <Button variant='secondary'>Secondary</Button>
    <Button variant='ghost'>Ghost</Button>
    <Button variant='destructive'>Destructive</Button>
    <Button variant='link'>Link</Button>
  </div>
);

export const Sizes = () => (
  <div className='flex flex-wrap items-center gap-3'>
    <Button size='lg'>Large</Button>
    <Button size='default'>Default</Button>
    <Button size='xs'>Extra Small</Button>
    <Button size='sm'>Small</Button>
  </div>
);

export const Interactive = () => {
  const [count, setCount] = useState(0);
  return (
    <Button onClick={() => setCount(c => c + 1)}>
      Clicked {count} {count === 1 ? 'time' : 'times'}
    </Button>
  );
};
