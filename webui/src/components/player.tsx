"use client";
import React, { useState } from "react";
import InputComponent from "@/components/InputComponent";
import ImageDisplayComponent from "@/components/ImageDisplayComponent";
import { MessageProvider } from "@/components/MessageContext";
import PlayerAnswer from "./player-answer";

export default function Player(props: { imagePath: string }) {
  return (
    <MessageProvider>
      <div className="flex relative min-h-screen">
        <div className="flex flex-col items-center justify-center w-full">
          <div className="relative flex justify-center items-center w-full">
            <div className="absolute left-0 flex flex-col items-center bg-pink-400"></div>
            <ImageDisplayComponent src={props.imagePath} />
            <div className="relative">
              <PlayerAnswer />
            </div>
            <InputComponent character={"胡桃"} />
          </div>
        </div>
      </div>
    </MessageProvider>
  );
}
