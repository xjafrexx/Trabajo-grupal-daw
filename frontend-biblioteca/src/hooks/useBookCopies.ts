import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { libraryApi } from '../api/libraryApi'

export function useBookCopies() {
  return useQuery({
    queryKey: ['book-copies', 'list'],
    queryFn: () => libraryApi.getBookCopies(),
    staleTime: 1000 * 60 * 5,
  })
}

export function useBookCopyDetail(id: string) {
  return useQuery({
    queryKey: ['book-copies', 'detail', id],
    queryFn: () => libraryApi.getBookCopy(id),
    enabled: Boolean(id),
    staleTime: 1000 * 60 * 5,
  })
}

export function useCreateBookCopy() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.createBookCopy,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['book-copies', 'list'] })
    },
  })
}

export function useUpdateBookCopy() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: Parameters<typeof libraryApi.updateBookCopy>[1] }) => 
      libraryApi.updateBookCopy(id, data),
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({ queryKey: ['book-copies', 'list'] })
      queryClient.invalidateQueries({ queryKey: ['book-copies', 'detail', variables.id] })
    },
  })
}

export function useDeleteBookCopy() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.deleteBookCopy,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['book-copies', 'list'] })
    },
  })
}