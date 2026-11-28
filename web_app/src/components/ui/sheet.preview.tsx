import { Button } from '@/components/ui/button';
import { Field, FieldDescription, FieldGroup, FieldLabel } from '@/components/ui/field';
import { Input } from '@/components/ui/input';
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet';

export const Demo = () => (
  <Sheet>
    <SheetTrigger render={<Button variant='outline' />}>Open sheet</SheetTrigger>
    <SheetContent>
      <SheetHeader>
        <SheetTitle>Edit profile</SheetTitle>
        <SheetDescription>Update your details and save the changes.</SheetDescription>
      </SheetHeader>
      <FieldGroup className='px-4'>
        <Field>
          <FieldLabel htmlFor='sheet-name'>Name</FieldLabel>
          <Input id='sheet-name' defaultValue='Jane Doe' />
        </Field>
        <Field>
          <FieldLabel htmlFor='sheet-email'>Email</FieldLabel>
          <Input id='sheet-email' type='email' defaultValue='jane@example.com' />
          <FieldDescription>Used for account notifications.</FieldDescription>
        </Field>
      </FieldGroup>
      <SheetFooter>
        <Button>Save changes</Button>
        <SheetClose render={<Button variant='outline' />}>Cancel</SheetClose>
      </SheetFooter>
    </SheetContent>
  </Sheet>
);

export const Sides = () => (
  <div className='flex flex-wrap items-center gap-2'>
    {(['top', 'right', 'bottom', 'left'] as const).map(side => (
      <Sheet key={side}>
        <SheetTrigger render={<Button variant='outline' className='capitalize' />}>{side}</SheetTrigger>
        <SheetContent side={side}>
          <SheetHeader>
            <SheetTitle className='capitalize'>{side} sheet</SheetTitle>
            <SheetDescription>Slides in from the {side} edge of the viewport.</SheetDescription>
          </SheetHeader>
          <div className='px-4 text-sm text-muted-foreground'>
            Sheets are useful for panel content that should not block the whole page.
          </div>
          <SheetFooter>
            <SheetClose render={<Button variant='outline' />}>Close</SheetClose>
          </SheetFooter>
        </SheetContent>
      </Sheet>
    ))}
  </div>
);
