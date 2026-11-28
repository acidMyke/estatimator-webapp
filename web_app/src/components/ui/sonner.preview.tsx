import { toast } from 'sonner';

import { Button } from '@/components/ui/button';
import { Toaster } from '@/components/ui/sonner';

const saveProfile = () => new Promise<void>(resolve => setTimeout(resolve, 1500));

export const Demo = () => (
  <div className='flex flex-col gap-4'>
    <Toaster />
    <div className='flex flex-wrap items-center gap-2'>
      <Button variant='outline' onClick={() => toast.success('Changes saved.')}>
        Success
      </Button>
      <Button variant='outline' onClick={() => toast.info('A new version is available.')}>
        Info
      </Button>
      <Button variant='outline' onClick={() => toast.warning('Storage is almost full.')}>
        Warning
      </Button>
      <Button variant='outline' onClick={() => toast.error('Something went wrong.')}>
        Error
      </Button>
      <Button variant='outline' onClick={() => toast.loading('Uploading...', { duration: 2000 })}>
        Loading
      </Button>
    </div>
    <div className='flex flex-wrap items-center gap-2'>
      <Button
        variant='secondary'
        onClick={() =>
          toast('Listing deleted.', {
            description: 'The listing was moved to the trash.',
            action: { label: 'Undo', onClick: () => toast.success('Listing restored.') },
          })
        }
      >
        With action
      </Button>
      <Button
        variant='secondary'
        onClick={() =>
          toast.promise(saveProfile(), {
            loading: 'Saving profile...',
            success: 'Profile saved.',
            error: 'Could not save the profile.',
          })
        }
      >
        Promise
      </Button>
    </div>
  </div>
);
