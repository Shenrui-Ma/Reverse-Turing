import React, { useContext, useState } from "react";
import { MessageContext, MessageContextType } from "./MessageContext";
import CodeBlock from "./code-block";

interface BarQuestionProps {
  question_type: string;
}

function BarQuestion({ question_type }: BarQuestionProps) {
  const context = useContext(MessageContext);
  const [buttonText, setButtonText] = useState("Start!");

  if (!context) {
    return null; // 或者返回一个加载状态
  }

  const { message, setMessage } = context as MessageContextType;

  const fetchQuestion = () => {
    fetch("http://localhost:8000/question", {
      method: "POST",
      headers: {
        "Content-Type": "text/plain", // 修改 Content-Type 为 text/plain
      },
      body: question_type, // 直接传递字符串
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setMessage(data.result);
      })
      .catch((error) => console.error("Error fetching data:", error));
    console.log("Request sent");
  };

  const renderContent = (text: string) => {
    const parts = text.split(/(```[\s\S]*?```)/g); // 使用正则表达式分割文本
    console.log("Parts:", parts); // 打印 parts 数组
    return parts.map((part, index) => {
      if (part.startsWith("```") && part.endsWith("```")) {
        const code = part.slice(3, -3).trim(); // 去除反引号并去除首尾空白
        return <CodeBlock key={index} code={code} />;
      }
      return <p key={index}>{part}</p>;
    });
  };

  const handleButtonClick = () => {
    setButtonText("Next ->");
    fetchQuestion();
    console.log("Button clicked!");
  };

  return (
    <div className="flex items-center justify-center h-full">
      <div
        className="border-8 border-pink-400 rounded-lg p-4 m-4 bg-pink-200"
        style={{
          width: "750px",
          height: "150px",
          overflow: "auto",
          fontSize: "18px",
          fontFamily: "Arial, sans-serif",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          position: "relative", // 确保按钮在最前面
          zIndex: 10, // 提高按钮的层级
        }}
      >
        {message ? renderContent(message) : "Ready?"}
      </div>
      <button
        className="border-4 border-black rounded-lg p-4 bg-blue-500 text-white hover:bg-blue-700 ml-4"
        style={{ fontSize: "20px" }}
        onClick={handleButtonClick}
      >
        {buttonText}
      </button>
    </div>
  );
}

export default BarQuestion;
