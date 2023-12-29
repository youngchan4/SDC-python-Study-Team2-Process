import unittest
from asyncio import sleep
from socket import socket
from unittest.mock import Mock


class TestTransmitRepository(unittest.TestCase):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def callTestTransmitRepository(self, data):
        clientSocket = Mock()
        clientSocket.sendall = Mock()

        try:
            print("transmitter: 응답 준비")
            response = data

            if response is not None:
                responseStr = str(response)
                print(f"응답할 내용: {response}")
                clientSocket.sendall(responseStr.encode())

        except (socket.error, BrokenPipeError) as exception:
            print(f"사용자 연결 종료")
            return None

        except socket.error as exception:
            print(f"전송 중 에러 발생: str{exception}")

        except Exception as exception:
            print("원인을 알 수 없는 에러가 발생하였습니다")

        finally:
            sleep(0.5)

    def testTransmitRepository(self):
        clientSocket = Mock()
        clientSocket.sendall = Mock()

        try:
            print("transmitter: 응답 준비")
            response = self.__transmitQueue.get()

            if response is not None:
                responseStr = str(response)
                print(f"응답할 내용: {response}")
                clientSocket.sendall(responseStr.encode())

        except (socket.error, BrokenPipeError) as exception:
            print(f"사용자 연결 종료")
            return None

        except socket.error as exception:
            print(f"전송 중 에러 발생: str{exception}")

        except Exception as exception:
            print("원인을 알 수 없는 에러가 발생하였습니다")

        finally:
            sleep(0.5)