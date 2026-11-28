import { Badge } from '@/components/ui/badge';
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';

const listings = [
  { id: '1', address: '12 Orchard Road', status: 'Active', price: 'S$ 1,250,000', variant: 'default' },
  { id: '2', address: '88 Marine Parade', status: 'Pending', price: 'S$ 640,000', variant: 'secondary' },
  { id: '3', address: '5 Bukit Timah Lane', status: 'Withdrawn', price: 'S$ 260,000', variant: 'destructive' },
] as const;

export const Demo = () => (
  <Table>
    <TableCaption>Recent listings from your workspace.</TableCaption>
    <TableHeader>
      <TableRow>
        <TableHead>Listing</TableHead>
        <TableHead>Status</TableHead>
        <TableHead className='text-right'>Price</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      {listings.map(listing => (
        <TableRow key={listing.id}>
          <TableCell className='font-medium'>{listing.address}</TableCell>
          <TableCell>
            <Badge variant={listing.variant}>{listing.status}</Badge>
          </TableCell>
          <TableCell className='text-right'>{listing.price}</TableCell>
        </TableRow>
      ))}
    </TableBody>
    <TableFooter>
      <TableRow>
        <TableCell colSpan={2}>Total</TableCell>
        <TableCell className='text-right'>S$ 2,150,000</TableCell>
      </TableRow>
    </TableFooter>
  </Table>
);

export const SelectedRow = () => (
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead>Listing</TableHead>
        <TableHead className='text-right'>Price</TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow data-state='selected'>
        <TableCell className='font-medium'>12 Orchard Road</TableCell>
        <TableCell className='text-right'>S$ 1,250,000</TableCell>
      </TableRow>
      <TableRow>
        <TableCell className='font-medium'>88 Marine Parade</TableCell>
        <TableCell className='text-right'>S$ 640,000</TableCell>
      </TableRow>
    </TableBody>
  </Table>
);
