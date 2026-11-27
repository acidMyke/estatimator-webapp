import { createFileRoute } from '@tanstack/react-router';

import { PlaceholderPage } from '@/components/blocks/placeholder-page';

export const Route = createFileRoute('/_public/about')({
  component: RouteComponent,
});

function RouteComponent() {
  return <PlaceholderPage title='About'></PlaceholderPage>;
}
