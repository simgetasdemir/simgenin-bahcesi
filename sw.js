// Petalpop çevrimdışı önbellek: aynı sitedeki dosyalar önbellekten, gerisi ağdan.
const C='petalpop-v1';
const CORE=['./','./index.html','./manifest.webmanifest','./icons/icon-192.png','./icons/icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET')return;
  const same=new URL(r.url).origin===location.origin;
  // Sayfa: önce ağ (güncel sürüm), olmazsa önbellek. Diğer dosyalar: önbellek, yoksa ağ ve kaydet.
  if(r.mode==='navigate'){e.respondWith(fetch(r).then(res=>{const cp=res.clone();caches.open(C).then(c=>c.put(r,cp));return res}).catch(()=>caches.match(r).then(m=>m||caches.match('./index.html'))));return}
  e.respondWith(caches.match(r).then(m=>m||fetch(r).then(res=>{if(res.ok&&(same||res.type==='cors')){const cp=res.clone();caches.open(C).then(c=>c.put(r,cp))}return res})));
});
