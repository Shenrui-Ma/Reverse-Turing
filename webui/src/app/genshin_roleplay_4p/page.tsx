"use client";
import NPC from "@/components/npc";
import Player from "@/components/player";
import BarQuestion from "@/components/bar-question";
import { MessageProvider } from "@/components/MessageContext";

export default function CodingQuestions4pPage() {
  const imagePaths = [
    "/images/hutao.png",
    "/images/chiori.png",
    "/images/arlecchino.png",
  ];

  return (
    <div className="flex flex-col h-full">
      <div className="fixed top-0 left-0 w-full z-50">
        <MessageProvider>
          <BarQuestion question_type="游戏背景：'''你要出一道题，几个玩家拿到你的题，扮演米哈游游戏《原神》的不同角色做角色扮演。'''你要做的：'''我需要你随机生成一个情景题，可以是现实的，比如哪种社交场景，，也可以是米哈游游戏《原神》世界观里的，可以引入原神里的角色、怪物、势力、国度等元素。出一道题，假设一个状况，问你如何应对，或做成什么反应，你会怎么想，之类的。字数不超过40字。'''" />
        </MessageProvider>
      </div>
      <div className="flex justify-center items-center h-screen mt-[-15vh]">
        {imagePaths.map((path, index) => (
          <MessageProvider key={index}>
            <NPC imagePath={path} />
          </MessageProvider>
        ))}
      </div>
      <div className="flex relative justify-center mt-[-55vh]">
        <Player imagePath="/images/罗志勇3.png" />
      </div>
    </div>
  );
}
