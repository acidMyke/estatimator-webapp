import { IconDots } from '@tabler/icons-react';

import { Button } from '@/components/ui/button';
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';

export const Demo = () => (
  <Card className='max-w-sm'>
    <CardHeader>
      <CardTitle>Team members</CardTitle>
      <CardDescription>Invite people to collaborate on this project.</CardDescription>
      <CardAction>
        <Button variant='ghost' size='icon-sm' aria-label='Open member options'>
          <IconDots />
        </Button>
      </CardAction>
    </CardHeader>
    <CardContent>
      <div className='flex flex-col gap-1.5'>
        <Label htmlFor='card-invite-email'>Email address</Label>
        <Input id='card-invite-email' type='email' placeholder='name@example.com' />
      </div>
    </CardContent>
    <CardFooter className='justify-end gap-2 border-t'>
      <Button variant='outline'>Cancel</Button>
      <Button>Send invite</Button>
    </CardFooter>
  </Card>
);

export const Small = () => (
  <Card size='sm' className='max-w-xs'>
    <CardHeader>
      <CardTitle>Small card</CardTitle>
      <CardDescription>Uses the compact spacing token.</CardDescription>
    </CardHeader>
    <CardContent>
      <p className='text-muted-foreground'>Tighter padding is useful for dense dashboards and side panels.</p>
    </CardContent>
  </Card>
);

export const Stats = () => (
  <div className='flex flex-wrap gap-4'>
    <Card className='w-48'>
      <CardHeader>
        <CardDescription>Active listings</CardDescription>
        <CardTitle className='text-2xl'>1,284</CardTitle>
      </CardHeader>
      <CardContent>
        <p className='text-xs text-muted-foreground'>+12% from last month</p>
      </CardContent>
    </Card>
    <Card className='w-48'>
      <CardHeader>
        <CardDescription>Average price</CardDescription>
        <CardTitle className='text-2xl'>S$ 512k</CardTitle>
      </CardHeader>
      <CardContent>
        <p className='text-xs text-muted-foreground'>+3.4% from last month</p>
      </CardContent>
    </Card>
  </div>
);
