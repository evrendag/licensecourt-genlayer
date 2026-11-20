import {studioDevnet} from "genlayer-js/chains";
const id=Number(process.env.NEXT_PUBLIC_GENLAYER_CHAIN_ID??"61997");
const rpc=process.env.NEXT_PUBLIC_GENLAYER_RPC_URL??"https://studio-next.genlayer.com/api";
export const GENLAYER_CHAIN={...studioDevnet,id,name:"GenLayer Studio Next",rpcUrls:{default:{http:[rpc]}},nativeCurrency:{name:"GEN",symbol:"GEN",decimals:18}};
