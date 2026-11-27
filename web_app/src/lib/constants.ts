import { linkOptions } from '@tanstack/react-router';

export const PUBLIC_NAVIGATIONS = linkOptions([
  {
    to: '/about',
    label: 'About',
    showHeader: true,
    showFooter: true,
  },
  {
    to: '/login',
    label: 'Login',
    showHeader: true,
    showFooter: false,
  },
  {
    to: '/register',
    label: 'Register',
    showHeader: true,
    showFooter: false,
  },
]);
