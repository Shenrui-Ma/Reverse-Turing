import React, { useContext, useEffect } from "react";
import { MessageContext, MessageContextType } from "./MessageContext";
import CodeBlock from "./code-block";

interface BarQuestionProps {
  question_type: string;
}

function BarQuestion({ question_type }: BarQuestionProps) {
  const context = useContext(MessageContext);

  if (!context) {
    return null; // 或者返回一个加载状态
  }

  const { message, setMessage } = context as MessageContextType;

  useEffect(() => {
    fetch("http://localhost:8000/get_question", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question_type }), // 这里可以根据需要修改默认消息
    })
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.result);
      })
      .catch((error) => console.error("Error fetching data:", error));
    console.log("useEffect一次");
  }, [setMessage, question_type]);

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

  return (
    <div
      className="border-8 border-pink-400 rounded-lg p-4 m-4 bg-pink-200"
      style={{
        width: "250px",
        height: "100px",
        overflow: "auto",
        fontSize: "18px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      {message ? renderContent(message) : "Ready?"}
    </div>
  );
}

export default BarQuestion;
