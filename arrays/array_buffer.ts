const a = new ArrayBuffer(6);

const a8 = new Uint8Array(a);

// walking 8 bits at a time
a8[0] = 45;

console.log(a);

a8[2] = 45;

console.log(a);

const a16 = new Uint16Array(a);

// walking 16 bits at a time
a16[2] = 0x4545;

console.log(a);

a16[2] = 0x45;

console.log(a);