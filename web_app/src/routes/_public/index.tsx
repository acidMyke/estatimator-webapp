import { createFileRoute } from '@tanstack/react-router';

import { PlaceholderPage } from '@/components/blocks/placeholder-page';

export const Route = createFileRoute('/_public/')({ component: Home });

function Home() {
  return <PlaceholderPage title='Landing'></PlaceholderPage>;
}
