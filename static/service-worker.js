console.log('Hello from sw.js');

importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.2.0/workbox-sw.js');

if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);

  workbox.precaching.precacheAndRoute([


  ]);

  workbox.routing.registerRoute(
    /\.(?:js|css|html)$/,
    workbox.strategies.staleWhileRevalidate({
      cacheName: 'static-resources',
    }),
  );

  workbox.routing.registerRoute(
    /^https:\/\/apprendrelerusse\.herokuapp\.com\//,
    workbox.strategies.staleWhileRevalidate({
      cacheName: 'static-resourceshtml',
    }),
  );



  workbox.routing.registerRoute(
    /^https:\/\/quizlet\.com\/481344669\/match\/embed\//
,
    workbox.strategies.staleWhileRevalidate({
      cacheName: 'static-quiz2',
    }),
  );

  workbox.routing.registerRoute(
    /https:\/\/quizlet\.com\//
,
    workbox.strategies.staleWhileRevalidate({
      cacheName: 'static-quiz',
    }),
  );

  workbox.routing.registerRoute(
    /\.(?:png|gif|jpg|jpeg|svg)$/,
    workbox.strategies.cacheFirst({
      cacheName: 'images',
      plugins: [
        new workbox.expiration.Plugin({
          maxEntries: 60,
          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
        }),
      ],
    }),
  );
 workbox.routing.registerRoute(
    new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
    workbox.strategies.cacheFirst({
      cacheName: 'googleapis',
      plugins: [
        new workbox.expiration.Plugin({
          maxEntries: 30,
        }),
      ],
    }),
  );



}else {
  console.log(`Boo! Workbox didn't load 😬`);
}





