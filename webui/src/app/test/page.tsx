"use client";
import NPC from "@/components/npc";
import Player from "@/components/player";

export default function TestPage() {
  const imagePaths = [
    "/images/hutao.png",
    "/images/chiori.png",
    "/images/arlecchino.png",
  ];

  return (
    <div className="flex flex-col h-full">
      <div className="flex justify-center items-center h-screen mt-[-25vh]">
        {imagePaths.map((path, index) => (
          <NPC key={index} imagePath={path} />
        ))}
      </div>
      <div className="flex relative justify-center mt-[-55vh]">
        <Player imagePath="/images/default.jpg" />
      </div>
    </div>
  );
}
